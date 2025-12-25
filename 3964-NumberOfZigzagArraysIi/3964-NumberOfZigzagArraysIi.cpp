// Last updated: 12/25/2025, 7:09:59 PM
#include <bits/stdc++.h>
using namespace std;

const int MOD = 1e9 + 7;

// Multiply two matrices
vector<vector<long long>> multiplyMatrix(const vector<vector<long long>> &x, const vector<vector<long long>> &y) {
    int m = x.size();
    vector<vector<long long>> ret(m, vector<long long>(m, 0));

    for (int row = 0; row < m; row++) {
        for (int j = 0; j < m; j++) {
            long long curr = 0;
            for (int i = 0; i < m; i++) {
                curr = (curr + x[row][i] * y[i][j] % MOD) % MOD;
            }
            ret[row][j] = curr;
        }
    }

    return ret;
}

// Fast matrix exponentiation
vector<vector<long long>> matrixPow(vector<vector<long long>> matrix, long long power) {
    if (power == 1) return matrix;

    long long halfPower = power / 2;
    vector<vector<long long>> ans = matrixPow(matrix, halfPower);
    ans = multiplyMatrix(ans, ans);
    if (power % 2) ans = multiplyMatrix(ans, matrix);

    return ans;
}

class Solution {
public:
    int zigZagArrays(long long n, int l, int r) {
        int m = r - l + 1;
        int m2 = 2 * m;

        vector<vector<long long>> matrix(m2, vector<long long>(m2, 0));

        for (int i = 0; i < m; i++) {
            if (i > 0) {
                for (int j = 0; j < i; j++) {
                    matrix[m + i][j] = 1;
                }
            }
            if (i + 1 < m) {
                for (int j = i + 1; j < m; j++) {
                    matrix[i][m + j] = 1;
                }
            }
        }

        matrix = matrixPow(matrix, n + 1);

        if (n % 2) {
            return (matrix[0][0] + matrix[m2 - 1][m2 - 1]) % MOD;
        } else {
            return (matrix[0][m2 - 1] + matrix[m2 - 1][0]) % MOD;
        }
    }
};
