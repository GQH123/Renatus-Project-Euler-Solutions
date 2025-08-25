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

#define maxn
#define maxm
#define maxs
#define maxb
#define inf 
#define eps
#define M 
#define ll long long int 

ll calPolygonal(int x, int type){
    return x * (1ll * (type - 2) * x + 4 - type) >> 1;
}

int minPolygonal(int x, int type) {
    int l = 1, r = x;
    while (l < r) {
        int mid = (l + r) >> 1;
        if (calPolygonal(mid, type) >= x) r = mid;
        else l = mid + 1;
    }
    return l;
}

bool isPolygonal(int x, int type) {
    // exists some integer n, that n * (type * n + 2 - type) / 2 = x ? 
    return calPolygonal(minPolygonal(x, type), type) == x;
}

#define piii pair<int, pii>
vector<piii> now;
bool hav[10];
void dfs(int pos, int bound) {
    if (pos == 7) {
        if (now[5].fi % 100 != now[0].fi / 100) return;
        int sum = 0;
        for (auto it: now) printf("%d(%d,%d) ", it.fi, it.se.fi, it.se.se), sum += it.fi;
        printf(": %d\n", sum);
        return;
    }
    rep(type, 3, 8) {   
        if (hav[type]) continue;
        hav[type] = 1;
        int l = minPolygonal(bound, type);
        int r = (pos == 1 ? minPolygonal(10000, type) : minPolygonal(bound+100, type));
        srep(i, l, r) {int d = calPolygonal(i, type); if (d % 100 < 10 || (pos != 1 && d <= now[0].fi)) continue; now.pb(piii(d, pii(type, i))), dfs(pos + 1, d % 100 * 100), now.pop_back();}
        hav[type] = 0;
    }
}

int main(){
    dfs(1, 1000);
	return 0;
}

