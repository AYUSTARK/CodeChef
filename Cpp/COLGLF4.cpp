//
// Developed by AYUSTARK
//
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
#define ll long long

int COLGLF4() {
    int t;
    cin >> t;
    while (t--) {
        ll int n, e, h, po, pm, pk;
        cin >> n >> e >> h >> po >> pm >> pk;
        vector<ll int> sol;
        vector<ll int> kvec;
        for (int i = 0; i <= n + 1; i++) {
            kvec.push_back(i);
        }
        for (ll int m = 0; m <= n; m++) {
            ll int idx1 = lower_bound(kvec.begin(), kvec.end(), (2 * n - e - 2 * m)) - kvec.begin();
            ll int idx2 = upper_bound(kvec.begin(), kvec.end(), (h - 3 * m)) - kvec.begin() - 1;
            if (idx2 < idx1 || idx1 == n + 1)
                continue;
            if (idx2 == n + 1 && (idx2 + 3 * m) > h)
                continue;
            ll int k;
            if (pk > po)
                k = (idx1 < (n - m) ? idx1 : (n - m));
            else
                k = (idx2 < (n - m) ? idx2 : (n - m));

            ll int o = n - k - m;
            if (k + 2 * m >= 2 * n - e && k + 3 * m <= h) {
                sol.push_back(po * o + pm * m + pk * k);
            }
        }
        if (sol.empty())
            cout << "-1" << endl;
        else {
            ll int min = sol[0];
            for (ll i : sol) {
                if (i < min) {
                    min = i;
                }
            }
            cout << min << endl;
        }
    }
    return 0;
}