# Last updated: 25/6/2025, 8:09:08 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        min_stack = deque([])
        max_stack = deque([])
        
        prev = 0
        ret = 1
        for i in range(n):
            while max_stack and nums[max_stack[-1]] < nums[i]:
                max_stack.pop()
            
            while min_stack and nums[min_stack[-1]] > nums[i]:
                min_stack.pop()
            
            max_stack.append(i)
            min_stack.append(i)

            while nums[max_stack[0]] - nums[min_stack[0]] > limit:
                prev += 1
                if max_stack[0] < prev:
                    max_stack.popleft()
                
                if min_stack[0] < prev:
                    min_stack.popleft()

            ret = cmax(ret, i - prev + 1)
        
        return ret