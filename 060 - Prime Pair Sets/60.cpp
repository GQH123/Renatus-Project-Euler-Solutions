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

#define maxn 200022
#define maxm
#define maxs
#define maxa 5
#define maxb
#define inf 
#define eps
#define M 
#define ll long long int 
#define int long long 

set<int> pset;
int pri[maxn];
int pct = 0;
bool pvis[maxn];
void init(){
    srep(i, 2, maxn) {
        if (!pvis[i]) pri[++pct] = i;
        rep(j, 1, pct) {
            if (i * pri[j] >= maxn) break;
            pvis[i * pri[j]] = 1;
            if (i % pri[j] == 0) break;
        }
    }
    rep(i, 1, pct) pset.insert(pri[i]);
}

int dep(int x) {
    int s = 1;
    while (x) {
        s *= 10;
        x /= 10;
    }
    return s;
}

bool chkprime(int x) {  
    if (x < maxn) return pset.count(x);
    rep(i, 1, pct) {
        int y = pri[i];
        if (y * y > x) break;
        if (x % y == 0) return false;
    }
    return true;
}

set<int> puz;
int puzlis[maxn], cp = 0;
int mod3[3];

int bound;
bool chk(int x, int y) {
    return chkprime(y * dep(x) + x) && chkprime(x * dep(y) + y);
}

struct ele{
    int rec[maxa];
    ele(){ memset(rec, 0, sizeof rec); }
    int sum(){
        int ans = 0;
        srep(i, 0, maxa) ans += rec[i];
        return ans;
    }
    void operator = (const ele b) {
        memcpy(rec, b.rec, sizeof rec);
    }
    bool operator < (ele b) {
        return sum() < b.sum();
    }
    void print(){
        printf("(%lld", rec[0]);
        srep(i, 1, maxa) {
            printf(", %lld", rec[i]);
        }
        printf("): %lld\n", sum());
    }
};
int ans = -1;
ele best, now;
vector<ele> all;
int allct = 0;
void dfs(int pos, int last){
    if (pos == maxa) {
        all.pb(now);
        allct++;
        int sum = now.sum();
        if (ans == -1 || sum < ans) {
            ans = sum;
            best = now;
        }
        return;
    }
    rep(i, last + 1, cp) {
        int x = puzlis[i];
        if (x >= bound) break;
        int mo3 = x % 3, mo4 = x & 3;
        if (mod3[(3 - mo3) % 3]) continue;
        srep(j, 0, pos) if (!chk(now.rec[j], x)) goto done; 
        now.rec[pos] = x;
        mod3[mo3]++;
        dfs(pos + 1, i);
        mod3[mo3]--;
        now.rec[pos] = 0;
        done:;
    }
}

signed main(){
    init();
    rep(i, 1, pct) {
        int s = 1, x = pri[i], y = 0;
        while (x) {
            int dig = x % 10;
            x /= 10;
            y += s * dig;
            s *= 10;
            if (dig == 0) continue;
            if (chkprime(x) && chkprime(y) && chkprime(y * dep(x) + x)) {   
                puz.insert(x);
                puz.insert(y);
            }
        }
    }
    
    printf("maxn: %d, puz: %lld, pset: %lld\n", maxn, (int)puz.size(), (int)pset.size());
    for (auto it: puz) printf("%lld ", it), puzlis[++cp] = it; printf("\n");
    
    bound = maxn;
    dfs(0, 0);
    
    printf("%lld\n", ans);
    best.print();
    printf("\ntotal number is: %lld\n", allct);
    sort(all.begin(), all.end());
    for (auto it: all) it.print();
    
	return 0;
}

