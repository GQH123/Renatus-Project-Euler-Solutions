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

struct cube{
    int op;
    cube(): op(0) {}
    cube(int op) : op(op) {}
    bool operator < (const cube b) const{
        return op < b.op;
    }
    bool operator == (const cube b) const{
        return op == b.op;
    }
    void set(int idx) {
        op |= (1 << idx);
    }
    void flip(int idx) {
        op ^= (1 << idx);
    }
    int get(int idx) {
        return (op >> idx) & 1;
    }
    int cnt() {
        int _op = op, num = 0;
        while (_op) num += (_op & 1), _op >>= 1;
        return num;
    }
};

struct cube_pair{
    cube x, y;
    cube_pair(){}
    cube_pair(cube x, cube y) : x(x), y(y){}
    bool operator < (const cube_pair b) const{
        return x == b.x ? y < b.y : x < b.x;
    }
    void norm(){
        if (y < x) swap(x, y);
    }
};

set<cube_pair> ans;
void dfs(cube x, cube y, int lastx = 0, int lasty = 0) {
    if (x.cnt() < 6) {
        rep(i, lastx, 9) {
            if (!x.get(i)) {
                x.set(i);
                dfs(x, y, i);
                x.flip(i);
            }
        }
        return;
    }
    if (y.cnt() < 6) {
        rep(i, lasty, 9) {
            if (!y.get(i)) {
                y.set(i);
                dfs(x, y, lastx, i);
                y.flip(i);
            }
        }
        return;
    }
    cube_pair r = cube_pair(x, y);
    r.norm();
    ans.insert(r);
}

int squ[] = {1, 4, 9, 16, 25, 36, 49, 64, 81};
int num69[] = {9, 16, 36, 49, 64};

int main(){
    //int mix = 6, miy = 6;
    rep(S, 0, (1 << 9)) {
        rep(T, 0, (1 << 5)) {
            cube x, y;
            int j = 0;
            srep(i, 0, 9) {
                int left = squ[i] / 10, right = squ[i] % 10;
                if (left == 6 || left == 9) {
                    if ((T >> j) & 1) left = 15 - left;
                    j += 1;
                }
                if (right == 6 || right == 9) {
                    if ((T >> j) & 1) right = 15 - right;
                    j += 1;
                }
                if ((S >> i) & 1) swap(left, right);
                x.set(left), y.set(right);
                if (x.cnt() > 6 || y.cnt() > 6) goto fail;
            }
            dfs(x, y);
            //printf("%d %d\n", x.cnt(), y.cnt());
            //mix = min(mix, x.cnt());
            //miy = min(miy, y.cnt());
            fail:;
        }
    }
    //printf("%d %d\n", mix, miy); // 4, 4
    printf("%d\n", (int)ans.size());
	return 0;
}

