// Last updated: 1/8/2026, 1:46:41 AM
1
2class Solution {
3public:
4  int minNumber(vector<int> &nums1, vector<int> &nums2) {
5    int arr1[10];
6    int arr2[10];
7    memset(arr1, 0, sizeof(arr1));
8    memset(arr2, 0, sizeof(arr2));
9
10    for (int num : nums1) {
11      arr1[num]++;
12    }
13
14    for (int num : nums2) {
15      arr2[num]++;
16    }
17
18    int first1 = -1;
19    int first2 = -1;
20    for (int i = 0; i < 10; i++) {
21      if (arr1[i] == 1 && arr2[i] == 1)
22        return i;
23    }
24
25    for (int i = 0; i < 10; i++) {
26      if (arr1[i] == 1) {
27        if (first2 != -1)
28          return first2 * 10 + i;
29        first1 = first1 == -1 || i < first1 ? i : first1;
30      }
31
32      if (arr2[i] == 1) {
33        if (first1 != -1)
34          return first1 * 10 + i;
35        first2 = first2 == -1 || i < first2 ? i : first2;
36      }
37    }
38    return 0;
39  }
40};
41