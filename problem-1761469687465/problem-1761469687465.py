# Last updated: 26/10/2025, 2:38:07 pm
class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        count = 0
        
        s = 0
        sl = SortedList()
        sl.add((0, -1))

        pre = [0] * n
        index = 0
        for i in range(1, n):
            if nums[i] != nums[i-1]:
                index = i
            
            pre[i] = index

        prev = -1
        for i in range(n):
            num = nums[i]
            s += num
            
            need = s % k

            l = sl.bisect_left((need, -1))
            r = sl.bisect_right((need, pre[i] - 1))
            # print(i, num, (l, r), sl, s)

            count += r - l
            
            sl.add((s % k, i))

        return count