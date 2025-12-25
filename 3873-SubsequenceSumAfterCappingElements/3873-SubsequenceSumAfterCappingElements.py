# Last updated: 12/25/2025, 7:11:18 PM
class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        # nums = [random.randrange(1, 4000 + 1) for _ in range(4000)]
        # k = 3867
        n = len(nums)

        nums.sort()
        # print(nums)
        
        dp = [[-1] * n for _ in range(k + 1)]
        
        def rec(index, rem):
            if rem < 0: return False
            if rem == 0: return True
            if index == -1: return False
            if dp[rem][index] != -1: return dp[rem][index]

            if rec(index - 1, rem):
                dp[rem][index] = 1
                return True
            if rem >= nums[index] and rec(index - 1, rem - nums[index]):
                dp[rem][index] = 1
                return True
            dp[rem][index] = 0
            return False

        ret = []
        for x in range(1, n + 1):
            index = bisect_left(nums, x)
            
            cnt = n - index
            index -= 1

            for i in range(0, cnt + 1):
                if rec(index, k - (x * i)):
                    ret.append(True)
                    break
            else:
                ret.append(False)

        return ret