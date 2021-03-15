//
// Developed by AYUSTARK
//
#include <bits/stdc++.h>
using namespace std;
#define ll long long int
bool solve()
{
    int r, c, x;
    cin >> r >> c >> x;
    vector<vector<int>> a(r, vector<int>(c)), b(r, vector<int>(c));
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            cin >> a[i][j];
    for (int i = 0; i < r; i++)
        for (int j = 0; j < c; j++)
            cin >> b[i][j];
    if (c < x and r < x)
    {
        // directly match
        for (int i = 0; i < r; i++)
            for (int j = 0; j < c; j++)
                if (a[i][j] != b[i][j])
                    return false;
    }
    else if (c < x)
    {
        // match row wise
        for (int i = 0; i < c; i++)
        {
            for (int j = 0; j <= r - x; j++)
            {
                // cout << j << " " << i << endl;
                if (a[j][i] != b[j][i])
                {
                    int diff = b[j][i] - a[j][i];
                    // cout << diff << endl;
                    for (int k = j; k < j + x; k++)
                        a[k][i] += diff;
                }
                if (j == r - x)
                {
                    for (int k = r - x + 1; k < r; k++)
                        if (a[k][i] != b[k][i])
                        {
                            // cout << a[k][i] << " != " << b[k][i] << endl;
                            return false;
                        }
                }
            }
        }
    }
    else if (r < x)
    {
        // match col wise
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j <= c - x; j++)
            {
                if (a[i][j] != b[i][j])
                {
                    int diff = b[i][j] - a[i][j];
                    for (int k = j; k < j + x; k++)
                        a[i][k] += diff;
                }
                if (j == c - x)
                {
                    for (int k = c - x + 1; k < c; k++)
                        if (a[i][k] != b[i][k])
                            return false;
                }
            }
        }
    }
    else
    {
        // both row and col
        // match row wise
        for (int i = 0; i < c; i++)
        {
            for (int j = 0; j <= r - x; j++)
            {
                if (a[j][i] != b[j][i])
                {
                    int diff = b[j][i] - a[j][i];
                    for (int k = j; k < j + x; k++)
                        a[k][i] += diff;
                }
                // if (j == r - x)
                // {
                //     for (int k = r - x + 1; k < r; k++)
                //         if (a[k][i] != b[k][i])
                //             return false;
                // }
            }
        }
        // match col wise
        // for (int i = 0; i < r; i++)
        // {
        //     for (int j = 0; j < c; j++)
        //         cout << a[i][j] << " ";
        //     cout << endl;
        // }
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j <= c - x; j++)
            {
                if (a[i][j] != b[i][j])
                {
                    int diff = b[i][j] - a[i][j];
                    for (int k = j; k < j + x; k++)
                        a[i][k] += diff;
                }
                if (j == c - x)
                {
                    for (int k = c - x + 1; k < c; k++)
                        if (a[i][k] != b[i][k])
                            return false;
                }
            }
        }
    }
    return true;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;
    while (T--)
    {
        if (solve())
            cout << "Yes" << endl;
        else
            cout << "No" << endl;
    }

    return 0;
}

