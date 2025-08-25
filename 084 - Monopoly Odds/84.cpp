#pragma GCC optimize(3)

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
#define inf 
#define eps
#define M 
#define ll long long int 
#define mo(x) (x = (x >= 40) ? x - 40 : x)

int num[maxn];
pii lis[maxn];
int eval_step = 100000000;

void print(int nowstep){
    printf("\n----- %d Steps -----\n", nowstep);
    srep(i, 0, 40) lis[i] = pii(num[i], i);
    sort(lis, lis + 40);
    srep(i, 0, 40) printf("%d: %.12f%%\n", lis[i].se, 100.0 * lis[i].fi / nowstep);
}

int roll(int side = 6){
    int a = rand() % side + 1;
    int b = rand() % side + 1;
    return (a + b) * ((a == b) ? -1 : 1);
}

int random(int l, int r) {
    assert(l <= r);
    return rand() % (r - l + 1) + l;
}

int R[] = {5, 15, 25, 35};
int U[] = {12, 28};
void play(int& nowp){
    if (nowp == 2 || nowp == 17 || nowp == 33) { //CC
        int _ = random(1, 16);
        switch(_) { 
            case 1: nowp = 0;   break;
            case 2: nowp = 10;  break;
        }
        return;
    }
    if (nowp == 7 || nowp == 22 || nowp == 36) { // CH
        int _ = random(1, 16);
        switch(_){
            case 1: nowp = 0;   break;
            case 2: nowp = 10;  break;
            case 3: nowp = 11;  break;
            case 4: nowp = 24;  break;
            case 5: nowp = 39;  break;
            case 6: nowp = 5;   break;
            case 7 ... 8: {
                if (nowp == 7) nowp = 15;
                else if (nowp == 22) nowp = 25;
                else if (nowp == 36) nowp = 5;
                break;
            }
            case 9:{
                if (nowp == 7) nowp = 12;
                else if (nowp == 22) nowp = 28;
                else if (nowp == 36) nowp = 12;
                break;
            }
            case 10: nowp = (nowp - 3 + 40), mo(nowp); break;
        }
        return;
    }
    if (nowp == 30) nowp = 10;
}

void Monte_Carlo(int step = 100000000){
    int nowp = 0;
    int double_cnt = 0;
    rep(_, 1, step) {
        int adv = roll();
        if (adv < 0) double_cnt += 1, adv = -adv;
        else double_cnt = 0;
        if (double_cnt == 3) {
            nowp = 10;
            double_cnt = 0;
        }
        else {
            nowp += adv;
            mo(nowp);
            play(nowp);
        }
        num[nowp] += 1;
        //if (_ % eval_step == 0) print(_); 
    }
    print(step);
}

int main(){
    srand(time(NULL));
    Monte_Carlo();
	return 0;
}

