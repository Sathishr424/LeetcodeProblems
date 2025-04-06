# Last updated: 6/4/2025, 7:32:53 am
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()

        visited = defaultdict(list)

        ret = [nums[0]]

        def rec(num, index):
            if index == n: return []
            if visited[num]: return visited[num]

            arr = []
            if nums[index] % num == 0:
                tmp = rec(nums[index], index+1)
                if len(tmp)+1 > len(arr):
                    arr = [nums[index]] + tmp
            
            tmp = rec(num, index+1)
            
            if len(tmp) > len(arr):
                arr = tmp
            
            visited[num] = arr
            return arr

        for i, num in enumerate(nums):
            arr = rec(num, i+1)
            if len(arr)+1 > len(ret):
                ret = [num] + arr
        
        return ret
            
