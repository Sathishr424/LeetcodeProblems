# Last updated: 13/6/2025, 9:08:35 am
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        n = len(nums)
        nums.sort()
        ret = 0

        l = 0
        r = (nums[-1] - nums[0]) + 1

        while l < r:
            mid = (l + r) // 2

            stack = deque([])
            
            cnt = 0
            for i in range(n):
                while stack and nums[i] - stack[0] > mid:
                    stack.popleft()
                    if stack:
                        stack.popleft()
                        cnt += 1
                stack.append(nums[i])
            
            while stack:
                stack.popleft()
                if stack:
                    stack.popleft()
                    cnt += 1

            if cnt >= p:
                r = mid
            else:
                l = mid + 1
        
        return l