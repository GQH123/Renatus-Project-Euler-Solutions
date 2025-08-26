def preprocess_combination_coefficients(n=120):
    """
        Preprocess the combination coefficients for the binomial theorem.
    """
    combination_coefficients = [[0] * n for _ in range(n)]
    combination_coefficients[0][0] = 1
    for i in range(1, n):
        combination_coefficients[i][0] = 1
        for j in range(1, i):
            combination_coefficients[i][j] = combination_coefficients[i-1][j-1] + combination_coefficients[i-1][j]
        combination_coefficients[i][i] = 1
    return combination_coefficients


combination_coefficients = preprocess_combination_coefficients()


def get_combination_coefficients(n, k):
    return combination_coefficients[n][k]


answer = 0
for num_digit in range(1, 101):
    # count of all number combination without all the same number
    x = get_combination_coefficients(num_digit + 9, 9) - 10
    # count of all number (except zero) combination without all the same number
    y = get_combination_coefficients(num_digit + 8, 8) - 9
    # count of combination with at least one zero, which can only be used as decreasing number
    answer += x - y
    # count of combination without zero, which can only be used as increasing number or decreasing number
    answer += y * 2
    # count of combination with all the same number (not zero)
    answer += 9

print(answer)
