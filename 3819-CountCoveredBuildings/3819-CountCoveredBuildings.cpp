// Last updated: 12/25/2025, 7:11:49 PM
class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        n++;
        vector<int> h_min(n, INT_MAX);
        vector<int> h_max(n, 0);
        vector<int> v_min(n, INT_MAX);
        vector<int> v_max(n, 0);

        for (auto& cord: buildings) {
            int x = cord[0];
            int y = cord[1];

            h_min[x] = min(h_min[x], y);
            h_max[x] = max(h_max[x], y);

            v_min[y] = min(v_min[y], x);
            v_max[y] = max(v_max[y], x);
            
        }

        int count = 0;
        for (auto& cord: buildings) {
            int x = cord[0];
            int y = cord[1];

            if (h_min[x] < y && h_max[x] > y && v_min[y] < x && v_max[y] > x) {
                count++;
            }
        }

        return count;
    }
};