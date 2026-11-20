# Time: O(amount * len(coins)), Space: O(amount)
# Reasoning: We fill a 1D table of size amount + 1 by iterating once through each coin across all target sub-amounts.
def count_ways_dp(amount, coins):
    if amount < 0:
        return 0
    ways = [0] * (amount + 1)
    ways[0] = 1

    for coin in coins:
        if coin <= 0:
            continue
        for a in range(coin, amount + 1):
            ways[a] = ways[a] + ways[a - coin]
    return ways[amount]


# Time: O(amount * len(coins)), Space: O(amount)
# Reasoning: For each sub-amount from 1 to amount, we check every coin in the list using a single table of length amount + 1.
def min_coins(amount, coins):
    if amount == 0:
        return 0
    if amount < 0 or not coins:
        return -1
    inf = amount + 1
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin > 0 and coin <= a:
                if dp[a - coin] + 1 < dp[a]:
                    dp[a] = dp[a - coin] + 1
    if dp[amount] == inf:
        return -1
    return dp[amount]


# Bonus: Returns (fewest_coins, list_of_coins_used) or (-1, [])
# Time: O(amount * len(coins)), Space: O(amount)
# Reasoning: Alongside the dp cost table, we maintain a parent-coin array of size amount + 1 to reconstruct the chosen coins in O(amount) steps.
def min_coins_with_path(amount: int, coins: list) -> tuple:
    if amount == 0:
        return (0, [])
    if amount < 0 or not coins:
        return (-1, [])

    inf = amount + 1
    dp = [inf] * (amount + 1)
    last_coin = [-1] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if 0 < coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1
                last_coin[a] = coin

    if dp[amount] == inf:
        return (-1, [])

    # Reconstruct which coins were picked
    chosen = []
    curr = amount
    while curr > 0:
        c = last_coin[curr]
        chosen.append(c)
        curr -= c

    return (dp[amount], chosen)


# --- Main Section (Testing & Explanations) ---
if __name__ == "__main__":
    # Prompt examples
    print("count_ways_dp(5, [1, 2, 5]):", count_ways_dp(5, [1, 2, 5]))                      # 4
    print("count_ways_dp(100, [1, 5, 10, 25, 50]):", count_ways_dp(100, [1, 5, 10, 25, 50])) # 292
    print("count_ways_dp(0, [1, 2]):", count_ways_dp(0, [1, 2]))                            # 1

    print("min_coins(11, [1, 2, 5]):", min_coins(11, [1, 2, 5]))                            # 3
    print("min_coins(100, [1, 5, 10, 25, 50]):", min_coins(100, [1, 5, 10, 25, 50]))         # 2
    print("min_coins(3, [2]):", min_coins(3, [2]))                                          # -1
    print("min_coins(0, [1]):", min_coins(0, [1]))                                          # 0

    # Large stress test required by prompt
    print("count_ways_dp(10000, [1, 5, 10, 25, 50]):", count_ways_dp(10000, [1, 5, 10, 25, 50]))

    # Why last week's recursive version could not finish amount = 10000:
    # 1. RecursionError: Subtracting 1 repeatedly creates a call stack 10,000 frames deep,
    #    exceeding Python's default recursion limit (~1,000 frames).
    # 2. Exponential work: Without a table/memoization, overlapping subproblems are recalculated
    #    billions of times instead of once per (amount, coin) state.

    # Custom test cases (including edge cases: empty coins, coins > amount, impossible target)
    print("Edge - empty coins:", count_ways_dp(5, []), min_coins(5, []))                    # 0, -1
    print("Edge - coins > amount:", count_ways_dp(3, [5, 10]), min_coins(3, [5, 10]))       # 0, -1
    print("Custom - exact single coin:", count_ways_dp(7, [7]), min_coins(7, [7]))          # 1, 1

    # Bonus test
    print("Bonus min_coins_with_path(11, [1, 2, 5]):", min_coins_with_path(11, [1, 2, 5]))  # (3, [1, 5, 5])
