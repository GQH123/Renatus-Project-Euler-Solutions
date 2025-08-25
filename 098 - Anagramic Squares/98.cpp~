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
    #define isletter(ch) ('A' <= ch && ch <= 'Z')
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

#define maxn 220
#define maxm
#define maxs
#define maxb
#define inf 
#define eps
#define M 
#define ll long long int 
#define sigma 26

char s[maxn];

struct ele{
    int num[sigma];
    ele() {memset(num, 0, sizeof num);}
    bool operator < (const ele b) const{
        srep(i, 0, sigma) if (num[i] != b.num[i]) return num[i] < b.num[i];
        return false;
    }
    bool check(){
        int cnt = 0;
        srep(i, 0, sigma) cnt += num[i] > 0;
        return cnt <= 10;
    }
};

struct res{
    string a, b; ll x, y, _x, _y;
    res(){a.clear(), b.clear(), x = y = _x = _y = 0;}
    res(string a, string b, ll x, ll y, ll _x, ll _y): a(a), b(b), x(x), y(y), _x(_x), _y(_y){}
    void print(){   
        if (x == 0) {cout << "Null"; return;}
        cout << a << "=" << x << "=" << _x << "^2";
        cout << ' ';
        cout << b << "=" << y << "=" << _y << "^2";
    }
    bool operator < (const res b) const{
        return max(x, y) < max(b.x, b.y);
    }
};

ll ten[maxn];
map<ele, vector<string>> _dict, dict;
map<char, int> nowv;
map<int, char> nowc;

res play_pair(string a, string b) {
    int l = a.length(), lower, upper;
    if (l & 1) {
        lower = (int)sqrt(ten[l - 1]);
        upper = (int)sqrt(ten[l]);
    }
    else {
        lower = (int)sqrt(ten[l - 1]) + 1;
        upper = (int)sqrt(ten[l]) - 1;
    }
    res op, _op;
    rep(i, lower, upper) {
        nowv.clear();
        nowc.clear();
        ll x = 1ll * i * i;
        int ptr = l - 1, _y; ll y = 0;
        bool first = true;
        while (x) {
            int d = x % 10; 
            if (nowc.count(d) && nowc[d] != a[ptr]) goto fail;
            nowc[d] = a[ptr];
            nowv[a[ptr]] = d;
            ptr -= 1;
            x /= 10;
        }
        assert(ptr == -1);
        //ll y = 0;
        for (auto c: b) {
            if (first) {
                if (nowv[c] == 0) goto fail;
                first = 0;
            }
            y = 10 * y + nowv[c];
        }
        _y = (int)sqrt(y);
        //int _y = sqrt(y);
        if (1ll * _y * _y == y) {
            _op = res(a, b, 1ll * i * i, y, i, _y);
            if (op < _op) op = _op;
        }
        fail:;
    }
    return op;
}

res play_group(vector<string> x) {
    int n = x.size();
    res op;
    srep(i, 0, n) srep(j, i + 1, n) {
        res _op = play_pair(x[i], x[j]);
        if (op < _op) op = _op;
    }
    return op;
}

int main(){
    ten[0] = 1;
    srep(i, 1, maxn) ten[i] = ten[i - 1] * 10;
    int n; read(n);
    rep(i, 1, n) {
        int l = reads(s + 1);
        ele op;
        rep(j, 1, l) {
            op.num[s[j] - 'A'] += 1;
        }
        if (!op.check()) continue;
        _dict[op].pb(string(s + 1));
    }
    for (auto it: _dict) {
        if (it.se.size() > 1) dict[it.fi] = it.se;
    }
    printf("groups: %d\n", (int)dict.size());
    
    ll mx = 0;
    for (auto it: dict) {
        bool first = true;
        for (auto it2: it.se) {
            if (first) cout << it2, first = false;
            else cout << ", " << it2;
        }
        cout << ": ";
        res op = play_group(it.se);
        op.print();
        cout << endl;
        
        mx = max(mx, max(op.x, op.y));
    }
    printf("Max: %lld\n", mx);
	return 0;
}

