def hanoi(n:int, source:str, target:str, helper:str) -> list[tuple[str, str]] :
    if n == 1:
        return [(source, target)]

    moves = []
    moves.extend(hanoi(n - 1, source, helper, target))
    moves.append((source, target))
    moves.extend(hanoi(n - 1, helper, target, source))
    return moves 

print(hanoi(1, "A", "C", "B")) 
print(hanoi(3, "A", "C", "B")) 

"""this is for the bonus part"""
def run_hanoi_bonus_proof():
    for n in range(1, 13):
        moves_list = hanoi(n, 'A', 'C', 'B')
        actual_count = len(moves_list)
        expected_count =(2 ** n) - 1

        if actual_count != expected_count:
            print('Mismatch found')
            return
    print('All counts perfectly match 2 ** n - 1!')

if __name__ == '__main__':
    run_hanoi_bonus_proof()





# print('-' * 10)
# print(run_hanoi_bonus_proof()) 
# print(run_hanoi_bonus_proof()) 
