// Last updated: 30/11/2025, 4:22:02 am
1class Solution {
2public:
3    int findMinimumTime(vector<vector<int>>& tasks) {
4        int n = tasks.size();
5        sort(tasks.begin(), tasks.end(), [](auto& a, auto& b) {
6            return a[0] < b[0];
7        });
8
9        unordered_set<int> used;
10
11        for (int i=n-1; i>=0; i--) {
12            auto& task = tasks[i];
13
14            int rem = task[2];
15            for (int time=task[0]; time<=task[1]; time++) {
16                if (used.find(time) != used.end()) {
17                    rem--;
18                }
19            }
20
21            for (int time=task[0]; time<=task[1]; time++) {
22                if (rem <= 0) break;
23                if (used.find(time) == used.end()) {
24                    used.insert(time);
25                    rem--;
26                }
27            }
28        }
29
30        return used.size();
31    }
32};