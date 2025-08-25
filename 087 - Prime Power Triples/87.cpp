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

#define maxn 8022
#define maxm
#define maxs
#define maxb
#define inf 
#define eps
#define M 
#define ll long long int 

int pri[maxn];
int pct = 0;
int phi[maxn];
bool pvis[maxn];
void pinit(){
    phi[1] = 1;
    pvis[1] = 1;
    srep(i, 2, maxn){
        if (!pvis[i]) pri[++pct] = i, phi[i] = i - 1;
        rep(j, 1, pct) {
            if (i * pri[j] >= maxn) break;
            pvis[i * pri[j]] = 1;
            if (i % pri[j] == 0) {
                phi[i * pri[j]] = phi[i] * pri[j];
                break;
            }
            phi[i * pri[j]] = phi[i] * (pri[j] - 1);
        }
    }
}

#define bound 50000000
bool good[bound];
/*
bool work(int n) {
    rep(i, 1, pct) {
        int x = pri[i], _x = x * x * x * x;
        if (_x >= n) break;
        rep(j, 1, pct) {
            int y = pri[j], _y = y * y * y;
            if (_y >= n - _x) break;
            int z = (int)sqrt(n - _x - _y);
            if (!pvis[z] && z * z == n - _x - _y) return true;
        }
    }
    return false;
*/
void work(){
    rep(i, 1, pct) {
        int x = pri[i], _x = x * x * x * x;
        if (_x >= bound) break;
        rep(j, 1, pct) {
            int y = pri[j], _y = y * y * y;
            if (_y >= bound - _x) break;
            rep(k, 1, pct){
                int z = pri[k], _z = z * z;
                if (_z >= bound - _x - _y) break;
                good[_x + _y + _z] = 1;
            }
        }
    }
}

int main(){
    pinit();
    int ans = 0;
    work();
    srep(i, 1, bound) ans += good[i];
    printf("%d\n", ans);
	return 0;
}

