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

#define maxn 100000000
#define maxm
#define maxs
#define maxb
#define inf 
#define eps
#define M 
#define ll long long int

int pri[maxn], cp = 0;
bool vis[maxn];
void init(){
	srep(i, 2, maxn) {
		if (!vis[i]) pri[++cp] = i;
		rep(j, 1, cp) {
			if (i * pri[j] >= maxn) break;
			vis[i * pri[j]] = 1;
			if (i % pri[j] == 0) break;
		}
	}
} 

vector<int> res;
int main(){
	init();
	srep(i, 1, maxn) {
		string s = to_string(i), _s = s;
		int l = s.length();
		for (int S = (1 << l) - 1; S; S--) {
			s = _s; int cnt = 0, mi = maxn; res.clear();
			if (S & 1) {
				rep(num, 1, 9) {
					srep(bit, 0, l) if ((S >> bit) & 1) s[bit] = '0' + num; 
					int x = atoi(s.c_str());
					if (!vis[x]) {
						cnt++;
						mi = min(mi, x);
						res.pb(x);
					}
				}
			}
			else {
				rep(num, 0, 9) {
					srep(bit, 0, l) if ((S >> bit) & 1) s[bit] = '0' + num; 
					int x = atoi(s.c_str());
					if (!vis[x]) {
						cnt++;
						mi = min(mi, x);
						res.pb(x);
					}
				}
			}
			if (cnt == 8) {
				for (auto it: res) printf("%d ", it); printf("\n"); 
				return 0;
			}
		}
	}
	return 0;
}

