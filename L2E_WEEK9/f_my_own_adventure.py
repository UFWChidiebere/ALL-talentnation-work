def create_world() -> dict:
    return {
        "ikeja_bus_stop": {
            "text": (
                "You are at Ikeja Underbridge at 4:30 PM on a Friday. Your flight leaves from VI soon!\n"
                "Exits: OSHODI (main road) or YABA (inner route)."
            ),
            "exits": {
                "oshodi": "oshodi_underbridge",
                "yaba": "yaba_tech_gate",
            },
            "item": None,
            "ending": None,
        },
        "oshodi_underbridge": {
            "text": (
                "Oshodi is buzzing with hawkers! A vendor is selling ice-cold bottled water.\n"
                "You can TAKE the item here, or head to TOLL (Third Mainland Bridge) or BACK to Ikeja."
            ),
            "exits": {
                "toll": "third_mainland_toll",
                "back": "ikeja_bus_stop",
            },
            "item": "cold_water",
            "ending": None,
        },
        "yaba_tech_gate": {
            "text": (
                "You reach Yaba. A retired conductor at a kiosk has a spare VIP commuter 'danfo_pass'.\n"
                "You can TAKE the item here, go to TOLL, peek down an ALLEY, or go BACK to Ikeja."
            ),
            "exits": {
                "toll": "third_mainland_toll",
                "alley": "secret_backstreet",
                "back": "ikeja_bus_stop",
            },
            "item": "danfo_pass",
            "ending": None,
        },
        "third_mainland_toll": {
            "text": (
                "You are at the Third Mainland Bridge entrance. LASTMA officers are checking for VIP commuter passes!\n"
                "Do you DRIVE onto the bridge or go BACK to Yaba?"
            ),
            "exits": {
                "drive": "lekki_phase_one",
                "back": "yaba_tech_gate",
            },
            "item": None,
            "ending": None,
        },
        "secret_backstreet": {
            "text": (
                "You found the hidden Sabo-Oyingbo express lane! Your cold water and danfo pass convinced\n"
                "a pro dispatch rider to escort you straight through the VIP lane.\n"
                "Type FINISH to cruise straight to Lekki!"
            ),
            "exits": {
                "finish": "lekki_phase_one",
            },
            "item": None,
            "ending": None,
        },
        "lekki_phase_one": {
            "text": (
                "*** YOU WIN! ***\n"
                "Your VIP danfo pass got you waved straight through the express lane! You made your flight with 20 minutes to spare."
            ),
            "exits": {},
            "item": None,
            "ending": "win",
        },
        "gridlock_trap": {
            "text": (
                "*** GAME OVER (LOSE) ***\n"
                "Without a VIP danfo pass, you were diverted into the bumper-to-bumper service lane.\n"
                "You are now listening to Lagos FM for the next four hours. Better luck next Friday!"
            ),
            "exits": {},
            "item": None,
            "ending": "lose",
        },
    }


def process_turn(rooms: dict, state: dict, raw_command: str) -> tuple:
    """Pure game-logic function: processes one player command and returns (updated_state, message)."""
    command = raw_command.strip().lower()

    # Copy state manually to keep function pure
    new_state = {
        "room": state["room"],
        "inventory": list(state["inventory"]),
        "turns": state["turns"],
        "max_turns": state["max_turns"],
        "status": state["status"],
    }

    if not command:
        return (new_state, "Please type a command (or 'quit' to exit).")

    if command == "quit":
        new_state["status"] = "quit"
        return (new_state, "You parked your car and called it a day. Thanks for playing!")

    if command == "inventory":
        items = ", ".join(new_state["inventory"]) if new_state["inventory"] else "nothing"
        return (new_state, f"You are carrying: {items}.")

    current_room = rooms[new_state["room"]]

    # Handle picking up an item
    if command == "take":
        item = current_room["item"]
        if item is None:
            return (new_state, "There is nothing useful to pick up here.")
        if item in new_state["inventory"]:
            return (new_state, f"You already picked up the {item}.")
        new_state["inventory"].append(item)
        return (new_state, f"Picked up: {item}! (Inventory: {new_state['inventory']})")

    # Handle movement between rooms
    if command in current_room["exits"]:
        next_room = current_room["exits"][command]

        # Two-item puzzle guard for the secret alley
        if next_room == "secret_backstreet":
            has_water = "cold_water" in new_state["inventory"]
            has_pass = "danfo_pass" in new_state["inventory"]
            if not (has_water and has_pass):
                return (
                    new_state,
                    "A scout blocks the secret alley: 'You need BOTH cold_water and a danfo_pass to take this shortcut!'",
                )

        # Single-item puzzle check when crossing the bridge
        if next_room == "lekki_phase_one" and "danfo_pass" not in new_state["inventory"]:
            next_room = "gridlock_trap"

        new_state["room"] = next_room
        new_state["turns"] += 1

        destination = rooms[next_room]
        if destination["ending"] is not None:
            new_state["status"] = destination["ending"]
            return (new_state, destination["text"])

        # Turn-limit check (Bonus)
        if new_state["turns"] >= new_state["max_turns"]:
            new_state["status"] = "lose"
            return (
                new_state,
                destination["text"] + "\n\n*** GAME OVER (LOSE) ***\nYou took 10 moves! Darkness fell and traffic froze completely.",
            )

        turns_left = new_state["max_turns"] - new_state["turns"]
        return (new_state, f"[Moves left: {turns_left}]\n{destination['text']}")

    valid_options = list(current_room["exits"].keys())
    if current_room["item"] and current_room["item"] not in new_state["inventory"]:
        valid_options.append("take")
    valid_options.extend(["inventory", "quit"])
    return (new_state, f"I didn't understand '{raw_command}'. Try: {', '.join(valid_options)}.")


# --- Main Game Loop ---
if __name__ == "__main__":
    world = create_world()
    game_state = {
        "room": "ikeja_bus_stop",
        "inventory": [],
        "turns": 0,
        "max_turns": 10,
        "status": "playing",
    }

    print("=== LAGOS FRIDAY TRAFFIC ESCAPE ===")
    print("Goal: Reach Lekki Phase 1 in under 10 moves! Type 'inventory' or 'quit' anytime.\n")
    print(f"[Moves left: {game_state['max_turns']}]")
    print(world[game_state["room"]]["text"])

    while game_state["status"] == "playing":
        user_input = input("\n> ")
        game_state, output_message = process_turn(world, game_state, user_input)
        print("\n" + output_message)
