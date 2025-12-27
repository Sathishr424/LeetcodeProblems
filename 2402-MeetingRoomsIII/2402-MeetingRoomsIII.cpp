// Last updated: 12/27/2025, 6:09:30 PM
1class Solution {
2public:
3    int mostBooked(int n, vector<vector<int>>& meetings) {
4        sort(meetings.begin(), meetings.end(), [](auto& a, auto& b) {
5            return a[0] < b[0];
6        });
7
8        vector<int> used(n, 0);
9        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> minHeap;
10        priority_queue<int, vector<int>, greater<int>> freeRooms;
11        for (int i=0; i<n; i++) {
12            freeRooms.push(i);
13        }
14        
15        for (auto& curr: meetings) {
16            while (!minHeap.empty() && minHeap.top().first <= curr[0]) {
17                freeRooms.push(minHeap.top().second);
18                minHeap.pop();
19            }
20
21            if (freeRooms.empty()) {
22                long long delay = minHeap.top().first - curr[0];
23                int room = minHeap.top().second;
24                minHeap.pop();
25                
26                used[room]++;
27                minHeap.push({curr[1] + delay, room});
28            } else {
29                used[freeRooms.top()]++;
30                minHeap.push({curr[1], freeRooms.top()});
31                freeRooms.pop();
32            }
33        }
34
35        int most_used = 0;
36        for (int i=0; i<n; i++) {
37            if (used[i] > used[most_used]) {
38                most_used = i;
39            }
40        }
41
42        return most_used;
43    }
44};