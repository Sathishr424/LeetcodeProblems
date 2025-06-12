# Last updated: 12/6/2025, 5:42:50 am
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            num = nums[i]
            tmp = 0
            ten = 1
            if num == 0: tmp = mapping[0]
            while num > 0:
                rem = num % 10
                num //= 10
                tmp += mapping[rem] * ten
                ten *= 10
            arr.append((tmp, i))
        arr.sort(key=lambda x: (x[0], x[1]) )
        return [nums[a[1]] for a in arr]