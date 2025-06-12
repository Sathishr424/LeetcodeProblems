// Last updated: 12/6/2025, 5:55:48 am
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        vector<int> totalNums(nums1);
        totalNums.insert(totalNums.end(), nums2.begin(), nums2.end());
        sort(totalNums.begin(), totalNums.end());
        if (totalNums.size() % 2 != 0)
            return totalNums[totalNums.size()/2];
        else
            return (double)((totalNums[(totalNums.size()-1)/2]) + (totalNums[totalNums.size()/2]))/2;
    }
};