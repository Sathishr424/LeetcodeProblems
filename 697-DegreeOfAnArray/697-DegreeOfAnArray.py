# Last updated: 12/6/2025, 5:47:34 am
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        hash = {}

        el = nums[0]
        freq = 1

        for i in range(n):
            if nums[i] in hash:
                hash[nums[i]][0] += 1
                hash[nums[i]][2] = i
                curr = hash[nums[i]]

                if curr[0] >= freq:
                    if curr[0] == freq:
                        if curr[2] - curr[1] < hash[el][2] - hash[el][1]:
                            freq = curr[0]
                            el = nums[i]
                    else:
                        freq = curr[0]
                        el = nums[i]

            else:
                hash[nums[i]] = [1, i, i]
        
        return (hash[el][2] - hash[el][1])+1
        
