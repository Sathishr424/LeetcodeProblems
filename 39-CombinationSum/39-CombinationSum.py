# Last updated: 9/5/2025, 9:01:38 pm
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        candidates.sort()


        def findCombination(ind: int, target: int):
            if target == 0:
                ans.append(ds[:])
                return
            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                ds.append(candidates[i])
                findCombination(i + 1, target - candidates[i])
                ds.pop()


        findCombination(0, target)
        return ans




if __name__ == "__main__":
    v = [10, 1, 2, 7, 6, 1, 5]
    solution = Solution()
    comb = solution.combinationSum2(v, 8)
    print(*comb)

        