# Last updated: 12/6/2025, 5:36:44 am
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)
        m_num = nums[0]
        cnt = 0

        for num in nums:
            if num == m_num: cnt += 1
            else: cnt -= 1
        
            if cnt == 0:
                m_num = num
                cnt = 1
        
        right = 0

        for num in nums:
            if num == m_num: right += 1
        
        left = 0
        for i in range(n-1):
            if nums[i] == m_num:
                right -= 1
                left += 1
            
            left_half = (i+1) // 2
            right_half = (n-i-1) // 2
            
            if left > left_half and right > right_half: return i
        
        return -1