from functools import lru_cache

combinations = []


def preprocess_combinations(n=100):  # calculate all combinations C(i, j) in range [0, n]
    global combinations
    combinations = [[0] * (n + 1) for _ in range(n + 1)]
    combinations[0][0] = 1
    for i in range(1, n + 1):
        combinations[i][0] = 1
        for j in range(1, i):
            combinations[i][j] = combinations[i-1][j-1] + combinations[i-1][j]
        combinations[i][i] = 1


catalan_numbers = []


def preprocess_catalan_numbers(n=50):
    global catalan_numbers
    catalan_numbers = [0] * (n + 1)
    catalan_numbers[0] = 1
    for i in range(1, n + 1):
        catalan_numbers[i] = combinations[2 * i][i] - combinations[2 * i][i + 1]


@lru_cache(maxsize=None)
def dp_L_must_lose_tail_count(n, prefix_sum, prefix_min):
    # if prefix_sum >= 0:
    #     return 0
    
    if n == 0:
        if prefix_sum < prefix_min:
            return 1
        else:
            return 0
    
    prefix_min = min(prefix_min, prefix_sum)
    return dp_L_must_lose_tail_count(n-1, prefix_sum+1, prefix_min) + dp_L_must_lose_tail_count(n-1, prefix_sum-1, prefix_min)


if __name__ == '__main__':
    preprocess_combinations()
    preprocess_catalan_numbers()
    
    N = 60
    answer = 2 ** N
    
    if N % 2 == 0:
        answer -= catalan_numbers[N//2-1]  # case 0: full parenthesis matching, first move player will lose
    
    L_must_lose_count = 0
    """
        case 1: the first letter after the last parenthesis matching (may be 0) is 'L', L will win if play first, L_must_lose += 0
        case 2: the first letter after the last parenthesis matching (may be 0) is 'R', L will lose if play second, and when no reverse parenthesis matching suffix appears after this 'R', L will also lose if play first, so we will count the number of such cases, L_must_lose += <as_below>
    """
    for i in range(0, N, 2):
        L_must_lose_count += catalan_numbers[i//2] * dp_L_must_lose_tail_count(N - i - 1, -1, 0)
    
    answer -= 2 * L_must_lose_count
    print(answer)
    # print(catalan_numbers)
    # print(dp_L_must_lose_tail_count(2, -1, 0))
    # print(dp_L_must_lose_tail_count(0, -1, 0))
    pass

"""
    A simpler conclusion, quoted from https://projecteuler.net/thread=948#443944
    
    > R going first has a win if and only if there is a proper prefix of the word where number of Rs is 
    number of Ls.

    > L going first has a win if and only if there is a proper suffix of the word where number of Ls is 
    number of Rs.
"""