# Last updated: 9/11/2025, 1:06:49 am
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        right = []
        index = n-1
        while index >= 0 and bisect_left(nums, nums[index] * 2) == n:
            right.append( nums[index] )
            index -= 1
        while index + 1 > len(right):
            right.append( nums[index] )
            index -= 1
            
        # print(index + 1, len(right), nums[:index+1], right[::-1])
        
        cnt = 0
        for i in range(index + 1):
            while right and right[-1] < nums[i] * 2: right.pop()
            if not right: break
            num = right.pop()
            # print(i, nums[i], num)
            cnt += 1

        return cnt * 2