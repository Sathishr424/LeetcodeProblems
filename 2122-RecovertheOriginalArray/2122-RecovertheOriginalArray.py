# Last updated: 16/8/2025, 1:33:06 pm
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        # N = 10**9
        # nums = [random.randrange(1, N+1) for _ in range(2000)]
        n = len(nums)
        nums.sort()
        m = n // 2

        diffs = {}
        for i in range(n):
            for j in range(i+1, n):
                diffs[nums[j] - nums[i]] = 1

        for k in diffs:
            if k == 0: continue
            ret = []

            freq = defaultdict(int)
            for i in range(n):
                freq[nums[i]] += 1
            
            higher = []
            lower = []
            for i in range(n):
                if freq[nums[i]] == 0:
                    higher.append(nums[i] - k)
                    continue
                freq[nums[i]] -= 1
                if freq[nums[i] + k]:
                    lower.append(nums[i] + k)
                    freq[nums[i] + k] -= 1
                else:
                    higher.append(nums[i] - k)
                    freq[nums[i]] += 1
                
            # print(k, lower, higher)
            if len(lower) == m:
                ret = []
                new_k = (lower[0] - higher[0]) // 2
                for i in range(m):
                    ret.append(lower[i] - new_k)
                    if lower[i] - new_k != higher[i] + new_k:
                        break
                else:
                    return ret

        return []
