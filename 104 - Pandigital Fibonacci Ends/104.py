def brute_force():
    import sys
    sys.set_int_max_str_digits(1000000)

    a, b = 0, 1
    index = 1

    while True:
        a, b = b, a + b
        index += 1
        print(f'index: {index}')
        # if index % 10000 == 0:
        #     print(f'index: {index}, b: {b}')
        # b_str = str(b)
        b_tail_str = str(b % 1000000000)  # key optimization
        if '0' in b_tail_str or set(b_tail_str) != set('123456789'):
            continue
        b_str = str(b)
        if '0' in b_str[:9]:
            continue
        if set(b_str[:9]) == set('123456789'):
            print(f'{b}, get {index}-th fibonacci number, containing {len(b_str)} digits')
            break


def fast_matrix2d_power(matrix, power):
    result = [[1, 0], [0, 1]]
    while power > 0:
        if power & 1 == 1:
            result = matrix2d_multiply(result, matrix)
        matrix = matrix2d_multiply(matrix, matrix)
        power >>= 1
    return result


def matrix2d_multiply(matrix1, matrix2):
    return [
        [matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0], matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]],
        [matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0], matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]]
    ]


def fast_fibonacci(n):  # for multiprocessing, however this is unnecessary after key optimization
    matrix = [[1, 1], [1, 0]]
    result = fast_matrix2d_power(matrix, n-1)
    return result[0][0]


if __name__ == '__main__':
    brute_force()
    # print(fast_fibonacci(20000))
    pass