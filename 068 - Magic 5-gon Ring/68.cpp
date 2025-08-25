#include <bits/stdc++.h>
#define rep(i, l, r) for (int i = l; i <= r; i++)
#define per(i, r, l) for (int i = r; i >= l; i--)
#define srep(i, l, r) for (int i = l; i < r; i++)
#define sper(i, r, l) for (int i = r; i > l; i--)
#define erep(i, x) for (int i = h[x]; i; i = e[i].next)
#define erep2(i, x) for (int& i = cur[x]; i; i = e[i].next)
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<double, double>
#define fi first
#define se second
#define ui unsigned int
#define ld long double
#define pb push_back
#define pc putchar
#define lowbit(x) (x & -x)
#define maxbuf 2000020
#define gc() ((p1 == p2 && (p2 = (p1 = buffer) + fread(buffer, 1, maxbuf, stdin), p1 == p2)) ? EOF : *p1++)
using namespace std;

namespace Fast_Read{
    char buffer[maxbuf], *p1, *p2;
    template<class T> void read_signed(T& x){
        char ch = gc(); x = 0; bool f = 1;
        while (!isdigit(ch) && ch != '-') ch = gc();
        if (ch == '-') f = 0, ch = gc();
        while ('0' <= ch && ch <= '9') x = (x << 1) + (x << 3) + ch - '0', ch = gc();
        x = (f) ? x : -x;
    }
    template<class T, class... Args> void read_signed(T& x, Args&... args){
        read_signed(x), read_signed(args...);
    }
    template<class T> void read_unsigned(T& x){
        char ch = gc(); x = 0;
        while (!isdigit(ch)) ch = gc(); 
        while (isdigit(ch)) x = (x << 1) + (x << 3) + ch - '0', ch = gc(); 
    }
    template<class T, class... Args> void read_unsigned(T& x, Args&... args){
        read_unsigned(x), read_unsigned(args...);
    }
    #define isletter(ch) ('a' <= ch && ch <= 'z')
    int read_string(char* s){
        char ch = gc(); int l = 0;
        while (!isletter(ch)) ch = gc();
        while (isletter(ch)) s[l++] = ch, ch = gc();
        s[l] = '\0'; return l;
    }
}using namespace Fast_Read; 

int _num[20];
template <class T> void write(T x, char sep = '\n'){	
	if (!x) {putchar('0'), putchar(sep); return;}
	if (x < 0) putchar('-'), x = -x;
	int c = 0;
	while (x) _num[++c] = x % 10, x /= 10;
	while (c) putchar('0' + _num[c--]); 
	putchar(sep);
}

#define read read_signed
#define reads read_string 
#define writes puts

#define maxn 11
#define maxm
#define maxs
#define maxb
#define inf 
#define eps
#define M 
#define ll long long int 

int n = 10;
string mx;

// (7n+6)/4
int s, ex;
string dp[maxn][maxn][maxn][1 << maxn];
pii vis[maxn][maxn][maxn][1 << maxn];
string DP(int p, int fin, int last, int use) {
    //printf("%d %d %d %d\n", p, fin, last, use);
    if (vis[p][fin][last][use] == pii(s, ex)) return dp[p][fin][last][use];
    vis[p][fin][last][use] = pii(s, ex);
    string& ans = dp[p][fin][last][use]; ans = "";
    assert(__builtin_popcount(use) == 11 - p);
    rep(i, 0, 9) {
        if (!((use >> i) & 1)) continue;
        int x = i + 1;
        int y = s - x - fin;
        if (y <= 0 || y >= 10 || x == y) continue;
        if (p != 10) if (!((use >> (y - 1)) & 1)) continue; 
        if (p == 10) if (y != last) continue;
        if (p != 2) if (x <= ex) continue;
        if (p == 2) {
            if (x == 10) continue; //if (y == 10) continue;
            if (DP(p+2, y, x, use^(1<<(x-1))^(1<<(y-1))) == "") continue;
            ans = max(ans, to_string(ex)+to_string(x)+to_string(y)+DP(p+2, y, x, use^(1<<(x-1))^(1<<(y-1))));
        }
        else if (p == 10){
            //if (y != last) continue;
            ans = max(ans, to_string(x)+to_string(fin)+to_string(last));
        }
        else {
            //if (y == 10) continue;
            if (DP(p+2, y, last, use^(1<<(x-1))^(1<<(y-1))) == "") continue;
            ans = max(ans, to_string(x)+to_string(fin)+to_string(y)+DP(p+2, y, last, use^(1<<(x-1))^(1<<(y-1))));
        }
    }
    return ans;
}

int main(){
    //cerr << max(string("abcd"), string("abcde")) << endl;
    string ans = "";
    rep(_s, n+3, (7*n+6)/4){    
        s = _s;
        rep(_ex, 1, 6){
            ex = _ex;
            ans = max(ans, DP(2, ex, 0, (1<<10)-1-(1<<(ex-1))));
        }
    }
    cout << ans << endl;
	return 0;
}

