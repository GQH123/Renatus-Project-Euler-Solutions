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

#define maxn 2022
#define maxm
#define maxs
#define maxb
#define maxp 3
#define inf 
#define eps
#define M 
#define ll long long int 

unsigned char a[maxn], b[maxn];
int cs = 0;

struct ele{
    unsigned char passwd[maxp];
    int alphanum = 0, sum = 0;
    bool operator < (ele b) {
        return alphanum < b.alphanum;
    }
    void print(){
        printf("(%c", passwd[0]);
        srep(i, 1, maxp) printf(", %c", passwd[i]);
        printf(")\n");
        rep(i, 1, cs) printf("%c", a[i] ^ passwd[i % 3]);
        printf("\nsum: %d\n\n", sum);
    }
};

ele now;
vector<ele> all;
void dfs(int pos){  
    if (pos == maxp) {
        cerr << all.size() << endl;
        all.pb(now);
        return;
    }
    for (unsigned char x = (unsigned char)'a'; x <= (unsigned char)'z'; x++) {
        int sum = 0, alphanum = 0;
        for (int i = pos; i < cs; i += maxp) {
            b[i] = a[i] ^ x;
            if (!isprint(b[i])) goto done;
            sum += b[i];
            alphanum += (isalpha(b[i]) ? 1 : 0);
        }
        now.passwd[pos] = x;
        now.sum += sum;
        now.alphanum += alphanum;
        dfs(pos + 1);
        now.sum -= sum;
        now.alphanum -= alphanum;
        now.passwd[pos] = 0;
        done:;
    }
}
int main(){
    freopen("p059_cipher.txt", "r", stdin);
    while (scanf("%u,", &a[cs++]) == 1); cs--;
    dfs(0);
    sort(all.begin(), all.end());
    for (auto it: all) it.print();
	return 0;
}

