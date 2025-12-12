// Last updated: 12/12/2025, 10:13:55 AM
1vector<int> split(const string& s, char delimiter) {
2    vector<int> tokens;
3    string token;
4    stringstream ss(s);
5    while (getline(ss, token, delimiter)) {
6        tokens.push_back(stoi(token.substr(2)));
7    }
8    return tokens;
9}
10
11class Solution {
12public:
13    vector<int> countMentions(int n, vector<vector<string>>& events) {
14        sort(events.begin(), events.end(), [](auto& a, auto& b) {
15            return stoi(a[1]) < stoi(b[1]) || (stoi(a[1]) == stoi(b[1]) && a[0] == "OFFLINE");
16        });
17
18        deque<pair<int, int>> again_online;
19        vector<int> online(n, 1);
20        vector<int> mentioned(n, 0);
21
22        for (auto& event: events) {
23            string status = event[0];
24            int timestamp = stoi(event[1]);
25            string ids = event[2];
26            // cout << status << " " << timestamp << " " << ids << endl;
27
28            while (again_online.size() && again_online[0].second <= timestamp) {
29                online[again_online[0].first] = 1;
30                again_online.pop_front();
31            }
32
33            if (status == "OFFLINE") {
34                again_online.push_back({stoi(ids), timestamp + 60});
35                online[stoi(ids)] = 0;
36                continue;
37            }
38
39            if (ids == "HERE") {
40                for (int i=0; i<n; i++) {
41                    if (online[i]) mentioned[i]++;
42                }
43            } else if (ids == "ALL") {
44                for (int i=0; i<n; i++) {
45                    mentioned[i]++;
46                }
47            } else {
48                vector<int> all_ids = split(ids, ' ');
49                for (int id: all_ids) {
50                    mentioned[id]++;
51                }
52            }
53        }
54
55        return mentioned;
56    }
57};