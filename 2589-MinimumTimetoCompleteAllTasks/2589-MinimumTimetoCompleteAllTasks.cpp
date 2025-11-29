// Last updated: 30/11/2025, 4:21:17 am
1class Solution {
2public:
3    int findMinimumTime(vector<vector<int>>& tasks) {
4        int n = tasks.size();
5        sort(tasks.begin(), tasks.end(), [](auto& a, auto& b) {
6            return a[0] < b[0];
7        });
8        unordered_map<int, int> freq;
9
10        for (auto task: tasks) {
11            for (int i=task[0]; i<=task[1]; i++) {
12                freq[i]++;
13            }
14        }
15
16        unordered_set<int> used;
17
18        for (int i=n-1; i>=0; i--) {
19            auto& task = tasks[i];
20
21            int rem = task[2];
22            for (int time=task[0]; time<=task[1]; time++) {
23                if (used.find(time) != used.end()) {
24                    rem--;
25                }
26            }
27
28            for (int time=task[0]; time<=task[1]; time++) {
29                if (rem <= 0) break;
30                if (used.find(time) == used.end()) {
31                    used.insert(time);
32                    rem--;
33                }
34            }
35        }
36
37        return used.size();
38    }
39};