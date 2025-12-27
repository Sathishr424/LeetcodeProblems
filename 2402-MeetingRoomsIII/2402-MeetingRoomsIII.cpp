// Last updated: 12/27/2025, 6:06:40 PM
1class Solution {
2public:
3    int mostBooked(int n, vector<vector<int>>& meetings) {
4        sort(meetings.begin(), meetings.end(), [](auto& a, auto& b) {
5            return a[0] > b[0];
6        });
7
8        vector<int> used(n, 0);
9        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> minHeap;
10        priority_queue<int, vector<int>, greater<int>> freeRooms;
11        for (int i=0; i<n; i++) {
12            freeRooms.push(i);
13        }
14        
15        while (!meetings.empty()) {
16            auto curr = meetings.back();
17
18            while (!minHeap.empty() && minHeap.top().first <= curr[0]) {
19                freeRooms.push(minHeap.top().second);
20                minHeap.pop();
21            }
22
23            if (freeRooms.empty()) {
24                long long delay = minHeap.top().first - curr[0];
25                used[minHeap.top().second]++;
26                minHeap.push({curr[1] + delay, minHeap.top().second});
27                minHeap.pop();
28            } else {
29                used[freeRooms.top()]++;
30                minHeap.push({curr[1], freeRooms.top()});
31                freeRooms.pop();
32            }
33            meetings.pop_back();
34        }
35
36        int most_used = 0;
37        for (int i=0; i<n; i++) {
38            if (used[i] > used[most_used]) {
39                most_used = i;
40            }
41        }
42
43        return most_used;
44    }
45};