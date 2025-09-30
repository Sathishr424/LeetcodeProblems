# Last updated: 30/9/2025, 9:58:22 pm
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        index = 0
        for i in range(n):
            if nums[i] == k:
                index = i
                break

        diff = [0] * n

        for i in range(n):
            if nums[i] < k:
                diff[i] = -1
            elif nums[i] > k:
                diff[i] = 1

        left = defaultdict(int)
        right = defaultdict(int)

        s = 0
        for i in range(index, -1, -1):
            s += diff[i]
            left[s] += 1

        s = 0
        for i in range(index, n):
            s += diff[i]
            right[s] += 1

        cnt = 0
        for val in left:
            need = -val
            need2 = need + 1
            
            cnt += left[val] * right[need]
            cnt += left[val] * right[need2]

        return cnt
            