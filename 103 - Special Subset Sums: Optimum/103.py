best_answer = []
best_answer_value = int(1e9)


def brute_force_dfs(seq, v_set):
    print(f'brute force: {seq}, {v_set}')
    if len(seq) == N:
        global best_answer, best_answer_value
        if sum(seq) < best_answer_value:
            best_answer_value = sum(seq)
            best_answer = seq.copy()
            return
    
    if len(seq) == 1:
        i_bound = 2 * seq[0]
    else:
        i_bound = seq[0] + seq[1]
        for i in range(2, len(seq)):
            i_bound = min(i_bound, sum(seq[:i+1]) - sum(seq[-i+1:]))
    
    for i in range(seq[-1] + 1, i_bound):
        failed = False
        for v in v_set:
            if i + v in v_set:
                failed = True
                break
        if failed:
            continue
        _v_list = []
        for v in v_set:
            _v_list.append(i + v)
        brute_force_dfs(seq + [i], v_set | set(_v_list))


if __name__ == '__main__':
    N, x0 = 7, 20  # best_answer: [20, 31, 38, 39, 40, 42, 45], value: 255
    # it simply follows the previous rules 😅
    brute_force_dfs([x0], {0, x0})
    print(f'best_answer: {best_answer}, value: {best_answer_value}')
    print(''.join([str(x) for x in best_answer]))
    pass