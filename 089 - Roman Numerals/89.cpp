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

#define maxn
#define maxm
#define maxs
#define maxb
#define inf 
#define eps
#define M 
#define ll long long int 

int getv(char ch) {
    switch(ch){
        case 'I': return 1;
        case 'V': return 5;
        case 'X': return 10;
        case 'L': return 50;
        case 'C': return 100;
        case 'D': return 500;
        case 'M': return 1000;
    }
    assert(false);
}

int getc(int x) {
    switch(x){
        case 1: return 'I';
        case 5: return 'V';
        case 10: return 'X';
        case 50: return 'L';
        case 100: return 'C';
        case 500: return 'D';
        case 1000: return 'M';
    }
    assert(false);
}

char s[2022];
int work(char* s, int l){
    int x = 0;
    srep(i, 0, l) {
        if (i < l - 1 && getv(s[i]) < getv(s[i + 1])) x -= getv(s[i]);
        else x += getv(s[i]);
    }
    l = 0;
    int base = 1000, _x = x;
    while (x) {
        int num = x / base;
        assert(0 <= num && num < 10);
        x -= num * base;
        if (base == 1000) {
            rep(i, 1, num) s[l++] = getc(base);
        }
        else {
            if (num == 9) s[l++] = getc(base), s[l++] = getc(base * 10);
            else if (num == 4) s[l++] = getc(base), s[l++] = getc(base * 5);
            else {
                if (num >= 5) s[l++] = getc(5 * base), num -= 5;
                rep(i, 1, num) s[l++] = getc(base);
            }
        }
        base /= 10;
    }
    s[l] = 0;
    return _x;
}

int main(){
    freopen("p089_roman.txt", "r", stdin);
    int n;
    read(n);
    int ans = 0;
    rep(i, 1, n) {  
        int l = reads(s);
        printf("%s: ", s);
        int x = work(s, l);
        printf("%s = %d\n", s, x);
        ans += (l - strlen(s));
    }
    printf("%d\n", ans);
	return 0;
}

