def check_special_set(seq):  # sorted sequence
    prefix = seq[0]
    suffix = 0
    for i in range(1, len(seq)):
        prefix += seq[i]
        suffix += seq[-i]
        if prefix <= suffix:
            return 0
    v_set = {0, seq[0]}
    for i in range(1, len(seq)):
        for v in v_set:
            if seq[i] + v in v_set:
                return 0
        v_set = v_set | {seq[i] + v for v in v_set}
    return sum(seq)


if __name__ == '__main__':
    answer = 0
    with open('input.txt', 'r') as f:
        seqs = [sorted([int(x) for x in line.strip().split(',')]) for line in f.read().split('\n') if line]
        for seq in seqs:
            answer += check_special_set(seq)
    print(answer)
    pass