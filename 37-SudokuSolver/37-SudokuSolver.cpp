// Last updated: 21/7/2025, 3:33:54 pm
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    void solveSudoku(vector<vector<char>>& board) {
        vector<int> boxes(9, 0);
        vector<int> rows(9, 0);
        vector<int> cols(9, 0);
        vector<pair<int, int>> need;
        int n = 9;

        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == '.') {
                    need.push_back({i, j});
                } else {
                    int pos = 1 << (board[i][j] - '1');
                    int box = (i / 3) * 3 + (j / 3);
                    rows[i] |= pos;
                    cols[j] |= pos;
                    boxes[box] |= pos;
                }
            }
        }

        function<bool(int)> dfs = [&](int index) {
            if (index == need.size()) return true;

            int i = need[index].first;
            int j = need[index].second;
            int box = (i / 3) * 3 + (j / 3);

            for (int val = 0; val < 9; ++val) {
                int pos = 1 << val;
                if ((rows[i] & pos) == 0 && (cols[j] & pos) == 0 && (boxes[box] & pos) == 0) {
                    int r = rows[i];
                    int c = cols[j];
                    int b = boxes[box];

                    rows[i] |= pos;
                    cols[j] |= pos;
                    boxes[box] |= pos;
                    board[i][j] = char('1' + val);

                    if (dfs(index + 1)) return true;

                    rows[i] = r;
                    cols[j] = c;
                    boxes[box] = b;
                    board[i][j] = '.';
                }
            }
            return false;
        };

        dfs(0);
    }
};