# Last updated: 21/10/2025, 1:27:08 pm
class Solution:
    def maxFrequency(self, nums: List[int], k: int, op: int) -> int:
        n = len(nums)

        nums.sort()
        # print(nums)
        ret = 1
        freq = defaultdict(int)

        i = 0
        while i < n:
            freq[nums[i]] += 1
            j = i + 1
            while j < n and nums[j] == nums[i]:
                j += 1
            
            dup = j - i - 1
            right = bisect_left(nums, nums[i] + k + 1)
            left = bisect_left(nums, nums[i] - k)

            left = min(op, i - left)
            right = min(op + dup, right - i - 1)
            ret = max(ret, left + 1, right + 1, min(left + right + 1, op + dup + 1))

            i = j
        
        if op < 2: return ret
        op -= 1
        i = 0
        while i < n:
            num = nums[i] + k
            dup = freq[num]
            right = bisect_left(nums, num + k + 1)
            left = bisect_left(nums, num - k)

            # print(i, num, (left, right, dup))

            left = min(op, i - left)
            right = min(op + dup, right - i - 1)
            # print(left, right)

            ret = max(ret, left + 1, right + 1, min(left + right + 1, op + dup + 1))

            i += 1
        
        return ret