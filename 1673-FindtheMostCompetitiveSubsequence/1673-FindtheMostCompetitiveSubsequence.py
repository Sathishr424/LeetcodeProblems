# Last updated: 9/4/2025, 4:50:21 pm
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            while stack and stack[-1] > num:
                if len(stack) <= k and (n - i) + len(stack) <= k: break
                stack.pop()
            
            stack.append(num)
            # if len(stack) <= k and (n - i - 1) + len(stack) <= k: break
            # print(stack)
        
        # print(stack)
        if len(stack) < k:
            stack = stack + nums[i+1:i+(k-len(stack))+1]
        elif len(stack) > k:
            while len(stack) > k: stack.pop()
        # print(len(stack), k)
        return stack