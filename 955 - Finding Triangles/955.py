import math


def check_triangle_number(x, method='binary_search'):
    if method == 'sqrt':
        m = int(math.sqrt(2 * x))
        if (m * (m + 1) // 2 == x):
            return True, m
        return False, None
    elif method == 'binary_search':
        l, r = 1, x
        while l < r:
            mid = (l + r) // 2
            if mid * (mid + 1) // 2 < x:
                l = mid + 1
            else:
                r = mid
        return (True, l) if l * (l + 1) // 2 == x else (False, None)


def brute_force_sequence():
    a, b = 3, 4
    triangle_number_count = 1
    b_is_triangle_numer = False
    seq_index = 1

    while True:
        a, b = b, (b + 1) if b_is_triangle_numer else (2 * b - a + 1)
        seq_index += 1
        b_is_triangle_numer, b_m = check_triangle_number(b)
        if b_is_triangle_numer:
            triangle_number_count += 1
            print(f'found {triangle_number_count}-th triangle number: ({b}, {b_m}) at index {seq_index}')
        if triangle_number_count == 70:
            break


"""
    found 2-th triangle number: (6, 3) at index 2
    found 3-th triangle number: (21, 6) at index 7
    found 4-th triangle number: (36, 8) at index 12
    found 5-th triangle number: (91, 13) at index 22
    found 6-th triangle number: (136, 16) at index 31
    found 7-th triangle number: (9316, 136) at index 166
    found 8-th triangle number: (154846, 556) at index 705
    found 9-th triangle number: (700336, 1183) at index 1749
    found 10-th triangle number: (1439056, 1696) at index 2964
    found 11-th triangle number: (369335431, 27178) at index 30089
    found 12-th triangle number: (577099351, 33973) at index 50473
    found 13-th triangle number: (901701811, 42466) at index 75952
    found 14-th triangle number: (1408928986, 53083) at index 107802
    found 15-th triangle number: (1449830476, 53848) at index 116846
    found 16-th triangle number: (23928296941, 218761) at index 328876
    found 17-th triangle number: (37387861426, 273451) at index 492946
    found 18-th triangle number: (168829016986, 581083) at index 1005666
    found 19-th triangle number: (460093231216, 959263) at index 1768901
    found 20-th triangle number: (110767449875176, 14884048) at index 16622005
    found 21-th triangle number: (114071019205006, 15104371) at index 19192440
"""


def brute_force_triangle_number_equation():
    for x in range(1, 101):
        y = 1
        # y = x
        # find z that x(x+1) + y(y+1) = z(z+1)
        while True:
            if (y + 1) * (y + 2) - y * (y + 1) > x * (x + 1):
                break
            is_triangle_numer, z = check_triangle_number(x * (x + 1) // 2 + y * (y + 1) // 2)
            if is_triangle_numer:
                print(f'found {x}, {y} -> {z}')
                break
            y += 1


def brute_force_sequence_by_enumerating_the_next_triangle_number():
    a, a_m = 3, 2
    triangle_number_count = 1
    seq_index = 0
    for i in range(70):
        next_a_m = a_m + 1
        next_a = a + next_a_m
        while not check_triangle_number(next_a - a)[0]:
            next_a_m += 1
            next_a += next_a_m
        seq_index_delta = check_triangle_number(next_a - a)[1]
        triangle_number_count += 1
        a_m = next_a_m
        a = a_m * (a_m + 1) // 2
        seq_index += seq_index_delta
        print(f'found {triangle_number_count}-th triangle number ({a}, {a_m}) at index {seq_index}')
        

if __name__ == '__main__':
    # brute_force_triangle_number_equation()
    brute_force_sequence_by_enumerating_the_next_triangle_number()
    pass
