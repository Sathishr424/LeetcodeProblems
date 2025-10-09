# Last updated: 10/10/2025, 12:38:53 am
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)

        freq = defaultdict(int)
        ret = 0
        pairs = 0
        left = 0
        count = 0
        for i in range(n):
            num = nums[i]
            freq[num] += 1
            pairs += freq[num] - 1
            while pairs >= k:
                count += 1
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
            
            # print(i, count, pairs, freq)
            ret += count
        return ret