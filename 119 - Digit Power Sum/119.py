full_sequence = []

n_digit = 2

while True:
    print(f'running for {n_digit} digits')
    part_sequence = []
    lower_bound = 10 ** (n_digit - 1)
    upper_bound = 10 ** n_digit
    for i in range(2, 9 * n_digit + 1):
        base = 1
        exponent = 0
        while base < upper_bound:
            if lower_bound <= base:
                if sum([int(c) for c in str(base)]) == i:
                    part_sequence.append((base, f'{base}={i}^{exponent}'))
            base *= i
            exponent += 1
    full_sequence += sorted(part_sequence, key=lambda x: x[0])
    if len(full_sequence) >= 30:
        break
    print(full_sequence)
    n_digit += 1


print(full_sequence[29])
