maxn = 20000022

dp = [0] * maxn
vis = [0] * maxn
dp[0] = 1
vis[0] = 1
def DP(x):
    if vis[x]: return dp[x]
    vis[x] = 1
    ans = 0
    s = 1
    d = 1
    for i in range(1, x + 1):
        d = i * (3 * i - 1) >> 1
        if x - d < 0: 
            dp[x] = ans
            return dp[x]
        ans += s * DP(x - d)
        d = i * (3 * i + 1) >> 1
        if x - d < 0: 
            dp[x] = ans
            return dp[x]
        ans += s * DP(x - d)
        s = -s
    dp[x] = ans
    return dp[x]
    
def run():
    for i in range(maxn):
        if DP(i) % 1000000 == 0:
            print('%d: %d' % (i, DP(i)))
            return
    print("Fail!")
    
run()
