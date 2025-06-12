# Last updated: 12/6/2025, 5:51:22 am
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        ret = []
        left = nums[0]
        right = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if left == right:
                    ret.append(str(left))
                else:
                    ret.append(f"{left}->{right}")
                left = nums[i]
                right = nums[i]
            else:
                right = nums[i]
        if left == right:
            ret.append(str(left))
        else:
            ret.append(f"{left}->{right}")
        return ret
                
