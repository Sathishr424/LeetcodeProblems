// Last updated: 12/23/2025, 12:54:45 PM
1class Solution {
2public:
3    int maxTwoEvents(vector<vector<int>>& events) {
4        int n = events.size();
5        vector<pair<int, int>> ends;
6        for (auto& event: events) {
7            ends.push_back({event[1], event[2]});
8        }
9
10        sort(events.begin(), events.end(), [](auto& a, auto& b) {
11            return a[0] < b[0];
12        });
13
14        sort(ends.begin(), ends.end(), [](auto& a, auto& b) {
15            return a.first < b.first;
16        });
17
18        vector<int> maxValues(n, 0);
19
20        int maxVal = 0;
21        for (int i=n-1; i>=0; i--) {
22            maxVal = max(maxVal, events[i][2]);
23            maxValues[i] = maxVal;
24        }
25
26        int index = 0;
27        int best = maxValues[0];
28        for (int i=0; i<n; i++) {
29            while (index < n && events[index][0] <= ends[i].first) {
30                index++;
31            }
32
33            if (index < n) {
34                best = max(best, ends[i].second + maxValues[index]);
35            }
36        }
37
38        return best;
39    }
40};