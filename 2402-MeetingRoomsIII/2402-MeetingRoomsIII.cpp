// Last updated: 12/27/2025, 6:01:09 PM
1class Solution {
2public:
3    int mostBooked(int n, vector<vector<int>>& meetings) {
4        sort(meetings.begin(), meetings.end(), [](auto& a, auto& b) {
5            return a[0] > b[0];
6        });
7
8        vector<int> free(n, 0);
9        vector<int> used(n, 0);
10        int freeRooms = n;
11        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> minHeap;
12        
13        while (!meetings.empty()) {
14            auto curr = meetings.back();
15
16            while (!minHeap.empty() && minHeap.top().first <= curr[0]) {
17                free[minHeap.top().second] = 0;
18                minHeap.pop();
19                freeRooms++;
20            }
21
22            long long delay = 0;
23            if (freeRooms == 0) {
24                delay = minHeap.top().first - curr[0];
25                free[minHeap.top().second] = 0;
26                minHeap.pop();
27                freeRooms++;
28            }
29
30            for (int i=0; i<n; i++) {
31                if (free[i] == 0) {
32                    free[i] = 1;
33                    used[i]++;
34                    freeRooms--;
35                    minHeap.push({curr[1] + delay, i});
36                    break;
37                }
38            }
39
40            meetings.pop_back();
41        }
42
43        int most_used = 0;
44        for (int i=0; i<n; i++) {
45            if (used[i] > used[most_used]) {
46                most_used = i;
47            }
48        }
49
50        return most_used;
51    }
52};