// Last updated: 12/6/2025, 5:36:40 am
class Solution {
public:
    int minimumIndex(vector<int>& nums) {
        int m_num = nums[0];
        int cnt = 0;
        int n = nums.size();

        for (int num: nums) {
            if (num == m_num) cnt++;
            else cnt--;

            if (cnt == 0) {
                m_num = num;
                cnt = 1;
            }
        }
        int right = 0;
        for (int num: nums) {
            right += num == m_num;
        }
        int left = 0;
        for (int i=0; i<n-1; i++) {
            if (nums[i] == m_num) {
                right--;
                left++;
            }

            int left_half = (i+1) / 2;
            int right_half = (n-i-1) / 2;

            if (left > left_half && right > right_half) return i;
        }

        return -1;
    }
};