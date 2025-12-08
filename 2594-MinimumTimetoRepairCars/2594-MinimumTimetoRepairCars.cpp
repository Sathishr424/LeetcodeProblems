// Last updated: 12/8/2025, 7:33:02 PM
1class Solution {
2public:
3    long long repairCars(vector<int>& ranks, int cars) {
4        long long left = 1, right = (long long)*min_element(ranks.begin(), ranks.end()) * cars * cars;
5        
6        auto can_repair_all = [&](long long time) {
7            long long total_cars_repaired = 0;
8            for (int rank : ranks) {
9                total_cars_repaired += sqrt(time / rank);
10                if (total_cars_repaired >= cars) return true;
11            }
12            return false;
13        };
14        
15        while (left < right) {
16            long long mid = (left + right) / 2;
17            if (can_repair_all(mid)) {
18                right = mid;
19            } else {
20                left = mid + 1;
21            }
22        }
23        
24        return left;
25    }
26};