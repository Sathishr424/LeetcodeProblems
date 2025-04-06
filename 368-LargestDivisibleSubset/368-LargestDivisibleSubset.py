# Last updated: 6/4/2025, 7:23:26 am
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nums.sort()
        # print(nums)

        graph = defaultdict(list)
        visited = defaultdict(list)

        ret = [nums[0]]
        def rec(x):
            if visited[x]: return visited[x]
            if x not in graph: return []

            arr = []

            for y in graph[x]:
                if y % x == 0:
                    tmp = rec(y)
                    if len(tmp)+1 > len(arr):
                        arr = [y] + tmp
            
            visited[x] = arr
            return arr

        for i in range(n):
            left = nums[i]
            for j in range(i+1, n):
                right = nums[j]

                if right % left == 0:
                    graph[left].append(right)
        
        # print(dict(graph))

        for num in graph:
            arr = rec(num)
            if len(arr)+1 > len(ret):
                ret = [num] + arr
        
        return ret
            
