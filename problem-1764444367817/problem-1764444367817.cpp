// Last updated: 30/11/2025, 12:56:07 am
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
11            while (index < 32) {
12                bits[index] += num & 1;
13                need += bits[index] & 1 ? 1 << index : 0;
14                num >>= 1;
15                index++;
16            }
17
18            count += freq[need];
19            freq[need]++;
20        }
21
22        return count;
23    }
24};