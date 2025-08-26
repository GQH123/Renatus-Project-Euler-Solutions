def preprocess_combination_coefficients(n=20):
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


def preprocess_higher_order_forward_differences_coefficients(n=20):
    """
        Preprocess the higher order forward differences coefficients for the binomial theorem.
    """
    higher_order_forward_differences_coefficients = [[0] * n for _ in range(n)]
    for i in range(n):
        d = 1
        for j in range(i+1):
            higher_order_forward_differences_coefficients[i][j] = get_combination_coefficients(i, j) * d
            d = -d
    return higher_order_forward_differences_coefficients


higher_order_forward_differences_coefficients = preprocess_higher_order_forward_differences_coefficients()


def get_higher_order_forward_differences_coefficients(k):
    return higher_order_forward_differences_coefficients[k]


def fit_terms_by_optimum_polynomial_use_higher_order_forward_differences(terms):
    """
        Simply, we can use Gaussian Elimination to solve the system of linear equations. However, the elimination coefficients can be pre-determined by higher order forward differences. In that case, we can directly solve the system of linear equations by multiplying the coefficients.
        
        For example, if we have the following terms:
        [1, 8, 27, 64, 125, ...]
        
        We can solve the system of linear equations w.r.t. the optimum polynomial coefficients (for example k=5) by using the following system of linear equations:
        a + b + c + d + e = 1
        16a + 8b + 4c + 2d + e = 8
        81a + 27b + 9c + 3d + e = 27
        256a + 64b + 16c + 4d + e = 64
        625a + 125b + 25c + 5d + e = 125
        
        Then we can calculate the value of 'a' by multiplying the coefficients to the equations if the higher order forward differences.
        [1, -4, 6, -4, 1]
        
        Which will eliminate the coefficients of 'b', 'c', 'd', and 'e' from the equations. After eliminating 'a', we can similarly calculate the value of all variables, using lower order differences coefficients.
        [1, -3, 3, -1]
        [1, -2, 1]
        [1, -1]
        
        In this way, we avoid using Gaussian Elimination and optimize the time complexity to O(k^2) (because only coefficients of the currently eliminated variable need to be stored and maintained).
    """
    
    degree = len(terms) - 1
    optimum_polynomial_coefficients = [0] * (degree + 1)
    
    for k in range(degree, -1, -1):
        equation_coefficients = get_higher_order_forward_differences_coefficients(k)
        equation_left_side = 0
        equation_right_side = 0
        for i in range(0, k+1):
            equation_left_side += equation_coefficients[i] * (i+1)**k
            equation_right_side += equation_coefficients[i] * terms[i]
        assert equation_right_side % equation_left_side == 0  # thinking: why the coefficients are always integers? (after a while, I found a proof which lead to another method to solve this problem, but the space is limited so I can't write it down here :) hint: 1.the original polynomial must be integer 2.try to construct lower-degree polynomial with zeros from 1 to k-1)
        optimum_polynomial_coefficients[k] = equation_right_side // equation_left_side
        for i in range(0, k+1):
            terms[i] = terms[i] - optimum_polynomial_coefficients[k] * (i+1)**k
    
    return optimum_polynomial_coefficients


def _test_fit_terms_by_optimum_polynomial_use_higher_order_forward_differences(generating_function):
    sequence = []
    for i in range(1, 20):
        sequence.append(generating_function(i))
        print(fit_terms_by_optimum_polynomial_use_higher_order_forward_differences(sequence.copy()))


def evaluate_polynomial(polynomial_coefficients, x):
    result = 0
    for i in range(len(polynomial_coefficients)-1, -1, -1):
        result = result * x + polynomial_coefficients[i]  # Horner's method
    return result


def calculate_badop_sum(generating_function, degree):
    sequence = []
    badop_sum = 0
    real_next_term = generating_function(1)
    for i in range(1, degree+1):
        sequence.append(real_next_term)
        optimum_polynomial_coefficients = fit_terms_by_optimum_polynomial_use_higher_order_forward_differences(sequence.copy())
        next_term = evaluate_polynomial(optimum_polynomial_coefficients, i+1)
        real_next_term = generating_function(i+1)
        if next_term != real_next_term:
            badop_sum += next_term
        else:
            print(f'catch equal next term: {next_term} at {i+1}')
    return badop_sum


if __name__ == "__main__":
    problem_set_generating_function = lambda i: i**10-i**9+i**8-i**7+i**6-i**5+i**4-i**3+i**2-i+1
    # _test_fit_terms_by_optimum_polynomial_use_higher_order_forward_differences(problem_set_generating_function)
    print(calculate_badop_sum(problem_set_generating_function, 10))
    pass