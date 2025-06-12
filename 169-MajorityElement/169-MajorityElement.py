# Last updated: 12/6/2025, 5:52:08 am
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        m_num = nums[0]

        for num in nums:
            if num == m_num:
                cnt += 1
            else:
                cnt -= 1
            
            if cnt == 0: 
                m_num = num
                cnt = 1
        
        return m_num