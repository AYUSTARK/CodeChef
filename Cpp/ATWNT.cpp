#pragma GCC target ("avx2")
#pragma GCC optimization ("O3")
#pragma GCC optimization ("unroll-loops")
#pragma GCC target ("sse4")

#include "bits/stdc++.h"

using namespace std;
#define w(t) int t;cin>>t;while(t--)
typedef int ll;
typedef vector<int> vi;
typedef pair<ll, ll> pll;
const long long int mod = 1e9 + 7;
#define sim template<class c
#define ris return*this
#define dor >debug &operator<<
#define eni(x)sim>typename enable_if<sizeof dud<c>(0)x 1,debug&>::type operator<<(c i){
sim>
struct rge {
    c b, e;
};

sim> rge<c> range(c i, c j) { return rge<c>{i, j}; }

sim> auto dud(c *x) -> decltype(cerr << *x, 0);

sim> char dud(...);

struct debug {
#ifdef TINDER
    eni(!=)cerr<<boolalpha<<i;ris;}eni(==)ris<<range(begin(i),end(i));}
    sim,class b dor(pair<b,c>d){ris<<"("<<d.first<<", "<<d.second<<")";}
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wstring-plus-int"
    sim dor(rge<c>d){*this<<"[";for(auto it=d.b;it!=d.e;++it)*this<<", "+2*(it==d.b)<<*it;ris<<"]";}
#pragma clang diagnostic pop
#else

    sim dor(const c &) { ris; }

#endif
};

#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wunused-parameter"

#pragma clang diagnostic pop

#define pt(x)cout<<((x))<<"\n";

template<typename T>
T power(T a, T b) {
    if (b == 0)return 1;
    if (b == 1)return a;
    else {
        T res = (power(a, b / 2));
        if (b % 2) { return (res * res * a); } else { return res * res; }
    }
}

template<typename T>
T power(T a, T b, T modulo) {
    if (b == 0)return 1;
    if (b == 1)return a;
    else {
        T res = (power(a, b / 2, modulo) % modulo);
        if (b % 2) { return ((((res % modulo) * (res % modulo)) % modulo) * (a % modulo)) % modulo; }
        else {
            return ((res % modulo) * (res % modulo)) % modulo;
        }
    }
}

template<typename T>
T gcd(T a, T b) {
    if (b == 0) { return a; }
    return gcd(b, a % b);
}

struct HASH {
    static uint64_t splitmix64(uint64_t x) {
        x += 0x9e3779b97f4a7c15;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9;
        x = (x ^ (x >> 27)) * 0x94d049bb133111eb;
        return x ^ (x >> 31);
    }

    size_t operator()(uint64_t x) const {
        static const uint64_t FIXED_RANDOM = chrono::steady_clock::now().time_since_epoch().count();
        return splitmix64(x + FIXED_RANDOM);
    }
};

ll n;
vector<vi> tree;
vi cc;
vector<unordered_map<ll, ll, HASH>> store;
vi shrink;
vector<set<pll>> already;

void read() {
    cin >> n;
    tree.resize(n + 1);
    cc.resize(n + 1, 0);
    store.resize(n + 1);
    shrink.resize(n + 1);
    already.resize(n + 1);
    for (int i = 2; i <= n; ++i) {
        ll x;
        cin >> x;
        tree[x].emplace_back(i);
        cc[x]++;
    }
}

void chain(ll nd) {
    shrink[nd] = nd;
    for (auto &child:tree[nd]) {
        chain(child);
        if (cc[nd] == 1)shrink[nd] = shrink[child];
    }
}

void DFS(ll nd) {
    for (auto &to:tree[nd]) {
        ll c = to;
        if (cc[nd] == 1)c = shrink[nd];
        if (cc[c] == 0) {
            store[nd][cc[nd]]++;
            store[c][1]++;
            continue;
        }
        DFS(c);
        for (auto &it:store[c]) { store[nd][cc[nd] * 1ll * it.first] += it.second; }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    read();
    chain(1);
    DFS(1);
    w(q) {
        ll nd, w;
        cin >> nd >> w;
        nd = shrink[nd];
        auto itr = already[nd].lower_bound(pll{w, -1});
        if (itr != already[nd].end() and itr->first == w) {
            pt(itr->second)
            continue;
        }
        ll p = 0ll;
        for (auto &i:store[nd]) { if (i.first and w % i.first == 0) { p += (w / i.first) * i.second * 1ll; }}
        already[nd].insert(pll{w, w - p});
        pt(w - p)
    }
    return 0;
}
