K = -1
current_best_answer = -1
best_answer_set = []


def dfs(x, v_set):
    v_set.append(x)
    
    global current_best_answer, best_answer_set
    # prune
    if current_best_answer != -1 and len(v_set)-1 >= current_best_answer:
        return
    
    if x == K:
        if current_best_answer == -1 or len(v_set)-1 < current_best_answer:
            current_best_answer = len(v_set)-1
            best_answer_set = v_set.copy()
        return
    
    # for v in v_set:
    for v in v_set[::-1]:  # key optimization, should try bigger value first
        if x + v > K:
            continue
        dfs(x + v, v_set.copy())  # we can further optimize by storing all optimal combinations of reaching a number and using DP-like implementation
    
    """ 
        This is in fact a classic problem called "Egyptian Multiplication".
        
        We simply use `x + v`, where `x` is the last element of the chain, and `v` is a node in previous chain, to make transition.
        
        However, this may lead to suboptimal results when considering star-chain (namely the sum of the last elements with others) only. Refer to https://projecteuler.net/thread=122#4254 or https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15251-s08/Site/Materials/Lectures/Lecture14/lecture14.pdf for more details.
        
        This quotation is from the discussion of the problem on Project Euler.
        
        > A couple of notes on this. 
         
        > Knuth's formula (48) on page 458 is not what I would call a formula: there are 105 exceptional cases.  This may have been a sensible economy when memory was in short supply: I believe he first did the calculation in the early 1960s.
        
        > Most solvers have been calculating "star chains", whereby a chain is extended by considering all possible sums of the last element with other elements, rather than all possible sums.  Surprisingly, there are minimal chains that are not star chains, but the first counterexample occurs for n=12509, way beyond the scope of this problem.  This concern was raised by DavidF: the solvers (including myself) who only considered star chains got lucky.
    """


if __name__ == '__main__':
    answer = 0
    for K in range(1, 200+1):
        current_best_answer = -1
        best_answer_set = []
        dfs(1, [])  # use list instead of set to optimize
        m_k = current_best_answer
        print(f'K: {K}, m_k: {m_k}, best_answer_set: {best_answer_set}')
        answer += m_k
    print(answer)
    pass
