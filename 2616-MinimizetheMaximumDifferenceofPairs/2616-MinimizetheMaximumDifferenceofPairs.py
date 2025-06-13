# Last updated: 13/6/2025, 9:08:16 am
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        ret = 0
        n = len(nums)

        # 5, 7, 8, 10
        # [1, 2, 1, 3, 0, 2, 1, 1, 2, 3]

        l = 0
        r = (nums[-1] - nums[0]) + 1

        while l < r:
            mid = (l + r) // 2
            # print(l, mid, r)

            stack = deque([])
            
            cnt = 0
            for i in range(n):
                while stack and nums[i] - stack[0] > mid:
                    stack.popleft()
                    if stack:
                        stack.popleft()
                        cnt += 1
                stack.append(nums[i])
                # print(stack, cnt)
            
            while stack:
                stack.popleft()
                if stack:
                    stack.popleft()
                    cnt += 1

            # print(cnt)

            if cnt >= p:
                r = mid
            else:
                l = mid + 1
        
        return l