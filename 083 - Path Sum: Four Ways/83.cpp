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

#define maxn 82
#define maxm
#define maxs
#define maxb
#define inf 
#define eps
#define M 
#define ll long long int 

int n, m;
int a[maxn][maxn];
int lpre[maxn][maxn];

/*
int dp[maxn][maxn][maxn];
bool vis[maxn][maxn][maxn];
int DP(int lay, int l, int r) {
    if (lay == n + 1) return 0;
    if (vis[lay][l][r]) return dp[lay][l][r];
    int& ans = dp[lay][l][r]; ans = 0;
    vis[lay][l][r] = 1;
    int layn_bound = 0;
    if (lay == n) layn_bound = m;
    rep(_l, 1, r) {
        rep(_r, max(_l, max(l, layn_bound)), m) {
            ans = max(ans, lpre[lay][_r] - lpre[lay][_l - 1] + DP(lay + 1, _l, _r));
        }
    }
    return ans;
}
*/

inline int value(int id) {
    return a[(id - 1) / m + 1][(id - 1) % m + 1];
}
priority_queue<pii> pq;
int d[maxn * maxn];
bool vis[maxn * maxn];

void upd(int x, int op) {
    if (vis[op]) return;
    int _d = d[x] + value(op);
    if (d[op] == -1 || _d < d[op]) d[op] = _d;
    pq.push(pii(-_d, op));
}

void Dij(int s){
    rep(i, 1, n * m) d[i] = -1, vis[i] = 0;
    d[s] = value(s);
    pq.push(pii(-d[s], s));
    while (!pq.empty()) {
        pii op = pq.top(); pq.pop();
        int x = op.se;
        if (vis[x]) continue;
        vis[x] = 1;
        if (x % m != 1) upd(x, x - 1);
        if (x % m != 0) upd(x, x + 1);
        if ((x - 1) / m != 0) upd(x, x - m);
        if ((x - 1) / m != n - 1) upd(x, x + m);
    }
}

int main(){
    freopen("p083_matrix.txt", "r", stdin);
    n = m = 80;
    rep(i, 1, n) rep(j, 1, m) read(a[i][j]); 
    //rep(i, 1, n) rep(j, 1, m) lpre[i][j] = lpre[i][j - 1] + a[i][j]; 
    //printf("%d\n", DP(1, 1, m));
    Dij(1);
    printf("%d\n", d[n * m]);
	return 0;
}

