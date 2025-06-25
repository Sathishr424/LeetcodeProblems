# Last updated: 25/6/2025, 7:58:05 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        min_stack = deque([])
        max_stack = deque([])
        
        prev = 0
        ret = 1
        for i in range(n):
            while max_stack and max_stack[-1][0] < nums[i]:
                max_stack.pop()
            
            while min_stack and min_stack[-1][0] > nums[i]:
                min_stack.pop()

            while max_stack and max_stack[0][1] < prev:
                max_stack.popleft()
            
            while min_stack and min_stack[0][1] < prev:
                min_stack.popleft()
            
            max_stack.append((nums[i], i))
            min_stack.append((nums[i], i))

            while max_stack[0][0] - min_stack[0][0] > limit:
                prev += 1
                while max_stack and max_stack[0][1] < prev:
                    max_stack.popleft()
                
                while min_stack and min_stack[0][1] < prev:
                    min_stack.popleft()

            ret = cmax(ret, i - prev + 1)
        
        return ret