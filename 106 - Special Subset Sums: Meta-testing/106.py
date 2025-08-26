def lowbit(x):
    return x & -x


bitmasks = []


def preprocess_bitmasks(n):
    global bitmasks
    bitmasks = [[] for _ in range(n+1)]
    for i in range(0, 1 << n):
        bitmasks[i.bit_count()].append(i)
    for _bitmasks in bitmasks:
        _bitmasks.sort()


def enumerate_subset_and_count_answer(n):
    answer = 0
    preprocess_bitmasks(n)
    for s in range(2, (n >> 1) + 1):
        for i in range(len(bitmasks[s])):
            for j in range(i+1, len(bitmasks[s])):
                bitmask_1 = bitmasks[s][i]
                bitmask_2 = bitmasks[s][j]
                if bitmask_1 & bitmask_2:
                    continue
                win, lose = True, True
                while bitmask_1:
                    lowbit_1 = lowbit(bitmask_1)
                    lowbit_2 = lowbit(bitmask_2)
                    assert lowbit_1 != lowbit_2
                    if lowbit_1 < lowbit_2:
                        win = False
                    else:
                        lose = False
                    bitmask_1 ^= lowbit_1
                    bitmask_2 ^= lowbit_2
                assert bitmask_2 == 0
                if not win and not lose:
                    answer += 1
    return answer


if __name__ == '__main__':
    print(enumerate_subset_and_count_answer(4))
    print(enumerate_subset_and_count_answer(7))
    print(enumerate_subset_and_count_answer(12))
    pass
