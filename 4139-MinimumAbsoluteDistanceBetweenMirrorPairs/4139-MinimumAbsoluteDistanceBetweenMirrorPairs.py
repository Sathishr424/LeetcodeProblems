# Last updated: 12/25/2025, 7:07:59 PM
class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)

        revs = defaultdict(list)
        for i, num in enumerate(nums):
            rev = 0
            while num:
                rem = num % 10
                rev = rev * 10 + rem
                num //= 10
        
            revs[rev].append(i)

        best = 10**20
        for i in range(n-1, -1, -1):
            num = nums[i]
            while revs[num] and revs[num][-1] >= i:
                revs[num].pop()

            if revs[num]:
                best = min(best, i - revs[num][-1])

        return -1 if best >= n else best