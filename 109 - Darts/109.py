from functools import lru_cache

possible_moves = []
for move_type in ['S', 'D', 'T']:
    for move_score in list(range(1, 21)) + [25]:
        if move_type == 'T' and move_score == 25:
            continue
        possible_moves.append((move_type, move_score))
possible_moves = sorted(possible_moves)


def get_move_score(move):
    if move[0] == 'S':
        return move[1]
    if move[0] == 'D':
        return 2 * move[1]
    if move[0] == 'T':
        return 3 * move[1]


def repr_move(move):
    return f'{move[0]}{move[1]}'


@lru_cache(maxsize=None)
def f(n):
    answer = 0
    for the_last_move in possible_moves:
        if the_last_move[0] != 'D' or get_move_score(the_last_move) > n:
            continue
        if get_move_score(the_last_move) == n:
            answer += 1
            # print(f'{repr_move(the_last_move)}', flush=True)
            continue
        rest_score = n - get_move_score(the_last_move)
        for the_first_move_index in range(len(possible_moves)):
            the_first_move = possible_moves[the_first_move_index]
            if get_move_score(the_first_move) > rest_score:
                continue
            if get_move_score(the_first_move) == rest_score:
                answer += 1
                # print(f'{repr_move(the_first_move)} {repr_move(the_last_move)}', flush=True)
                continue
            _rest_score = rest_score - get_move_score(the_first_move)
            for the_second_move_index in range(the_first_move_index, len(possible_moves)):
                the_second_move = possible_moves[the_second_move_index]
                if get_move_score(the_second_move) != _rest_score:
                    continue
                # print(f'{repr_move(the_first_move)} {repr_move(the_second_move)} {repr_move(the_last_move)}', flush=True)
                answer += 1
    return answer

if __name__ == '__main__':
    # print(f(6))
    answer = 0
    for i in range(1, 100):
        answer += f(i)
    print(answer)
    pass
