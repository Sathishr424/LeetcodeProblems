// Last updated: 30/11/2025, 12:48:09 am
1class Solution {
2public:
3    long long beautifulSubarrays(vector<int>& nums) {
4        vector<int> bits(32, 0);
5        unordered_map<long long, int> freq;
6        freq[0]++;
7        long long count = 0;
8        for (int num: nums) {
9            int index = 0;
10            long long need = 0;
11            while (num) {
12                bits[index] += num & 1;
13                num >>= 1;
14                index++;
15            }
16
17            for (int i=0; i<32; i++) {
18                if (bits[i] & 1) {
19                    need += 1 << i;
20                }
21            }
22
23            count += freq[need];
24            freq[need]++;
25        }
26
27        return count;
28    }
29};