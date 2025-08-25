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
    #define isletter(ch) ('0' <= ch && ch <= '9' || 'A' <= ch && ch <= 'Z')
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

#define vb vector<bool> 
#define vi vector<int> 
#define hand vector<vb>
#define max_value 14
#define min_value 2
#define max_suit  4
#define min_suit  1
#define for_value(x) per(x, max_value, min_value)
#define for_suit(x)  rep(x, min_suit, max_suit)
#define rank RANK

hand carda, cardb;

vi operator + (vi a, vi b) {
    a.insert(a.end(), b.begin(), b.end());
    return a;
}

bool operator < (vi a, vi b) {
    int l = min(a.size(), b.size());
    srep(i, 0, l) if (a[i] != b[i]) return a[i] < b[i]; 
    return a.size() < b.size();
}

int value(char ch) {
	if (isdigit(ch)) return ch - '0';
	switch(ch){
		case 'T': return 10;
		case 'J': return 11;
		case 'Q': return 12;
		case 'K': return 13;
		case 'A': return 14;
	}
	assert(false);
}

int suit(char ch) {
	switch(ch){
		case 'D': return 1;
		case 'C': return 2;
		case 'H': return 3;
		case 'S': return 4;
	}
	assert(false);
}

int rank(string res){
    if (res == "StraightFlush")     return 9;
    if (res == "FourofaKind")	    return 8;
    if (res == "FullHouse")	        return 7;
    if (res == "Flush")	            return 6;
    if (res == "Straight")	        return 5;
    if (res == "ThreeofaKind")	    return 4;
    if (res == "TwoPairs")	        return 3;
    if (res == "OnePair")	        return 2;
    if (res == "HighCard")	        return 1;
    assert(false);
}

vi _SameValueCheck(hand& card, int num) {
    for_value(v){ 
	    int ct = 0;
	    for_suit(s) ct += card[s][v];
	    if (ct >= num) {  
	        for_suit(s) {
	            if (!ct) break;
	            if (card[s][v]) card[s][v] = 0, ct--;
	        }
	        return vi{v};
	    }
	}
	return vi{0};
}

vi _SameSuitCheck(hand& card, int s, int num=5) { 
    vi res = {};
    int ct = 0;
    for_value(v) ct += card[s][v];
    if (ct == num) {
        for_value(v) if (card[s][v]) res.pb(v), card[s][v] = 0;
        return res;
    }
    return vi{0};
}

vi _ConsecutiveCheck(hand& card, int first_val, bool same_suit, int len=5){
    if (first_val > max_value-len+1) assert(false);
    vi res = {};
    if (same_suit) {    
        for_suit(s) {
            srep(i, 0, len) if (!card[s][first_val + i]) goto fail2;
            srep(i, 0, len) card[s][first_val + i] = 0;
            per(i, len-1, 0) res.pb(first_val + i); return res;
            fail2:;
        }
        return vi{0};
    }
    else {
        srep(i, 0, len) {
            for_suit(s) if (card[s][first_val + i]) goto cont1;
            return vi{0};
            cont1:;
        }
        srep(i, 0, len) for_suit(s) if (card[s][first_val + i]) card[s][first_val + i] = 0;
        per(i, len-1, 0) res.pb(first_val + i); return res;
    }
}

vi StraightFlush(hand& card) {	
	per(v, 10, 2) { vi d = _ConsecutiveCheck(card, v, true); if (d[0]) return d; } return vi{0};
}

vi FourofaKind(hand& card) {
    return _SameValueCheck(card, 4);
}

vi ThreeofaKind(hand& card) {
	return _SameValueCheck(card, 3);
}

vi OnePair(hand& card) {
	return _SameValueCheck(card, 2);
}

vi TwoPairs(hand& card) {
    hand _card = card;
	vi v1 = OnePair(card); if (!v1[0]) return vi{0};
	vi v2 = OnePair(card); if (!v2[0]) { card = _card; return vi{0}; }
    return v1 + v2;
}

vi FullHouse(hand& card) {
	hand _card = card;
	vi v1 = ThreeofaKind(card); if (!v1[0]) return vi{0};
	vi v2 = OnePair(card); if (!v2[0]) { card = _card; return vi{0}; }
    return v1 + v2;
}

vi Flush(hand& card) {
    for_suit(s) { vi d = _SameSuitCheck(card, s); if (d[0]) return d; } return vi{0};
}

vi Straight(hand& card) {
    per(v, 10, 2) { vi d = _ConsecutiveCheck(card, v, false); if (d[0]) return d; } return vi{0};
}

vi HighCard(hand& card) {
	for_value(v) for_suit(s) if (card[s][v]) {card[s][v] = 0; return vi{v};} return vi{0};
}

bool empty(hand& card) {
	for_suit(s) if (!card[s].empty()) return false; return true;
}

vi get_rank(hand& card){
    vi d;
    d = StraightFlush(card);    if (d[0]) return vi{rank("StraightFlush")} + d;
    d = FourofaKind(card);      if (d[0]) return vi{rank("FourofaKind")} + d;
    d = FullHouse(card);        if (d[0]) return vi{rank("FullHouse")} + d;
    d = Flush(card);            if (d[0]) return vi{rank("Flush")} + d;
    d = Straight(card);         if (d[0]) return vi{rank("Straight")} + d;
    d = ThreeofaKind(card);     if (d[0]) return vi{rank("ThreeofaKind")} + d;
    d = TwoPairs(card);         if (d[0]) return vi{rank("TwoPairs")} + d;
    d = OnePair(card);          if (d[0]) return vi{rank("OnePair")} + d;
    d = HighCard(card);         if (d[0]) return vi{rank("HighCard")} + d;
    assert(false);
    return vi{0};
}

int comp(hand& carda, hand& cardb) {
    vi da, db;
    do{
        da = get_rank(carda), db = get_rank(cardb);
        if (da < db) return -1;
        if (da > db) return 1;
    }
    while (!empty(carda) && !empty(cardb));
    return 0;
}

void init(hand& carda, hand& cardb) {
	carda.clear();
	cardb.clear();
	carda.resize(max_suit+1);
	cardb.resize(max_suit+1);
	for (auto& it: carda) it.resize(max_value+1);
	for (auto& it: cardb) it.resize(max_value+1);
}

void work(){
    freopen("p054_poker.txt", "r", stdin);
	int cnt = 0;
	rep(i, 1, 1000) {
		hand carda, cardb;
		init(carda, cardb);
		char s[5];
		rep(j, 1, 5) {
			reads(s + 1);
			carda[suit(s[2])][value(s[1])] = 1;
		}
		rep(j, 1, 5) {
			reads(s + 1);
			cardb[suit(s[2])][value(s[1])] = 1;
		}
		if (comp(carda, cardb) > 0) cnt++;
	}
	printf("%d\n", cnt);
}

int main(){ work(); return 0; }
