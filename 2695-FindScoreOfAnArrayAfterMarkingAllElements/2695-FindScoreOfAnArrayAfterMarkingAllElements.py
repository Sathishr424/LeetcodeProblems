# Last updated: 12/6/2025, 5:37:12 am
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        marked = []
        arr = []
        for i in range(n):
            arr.append((nums[i], i))
            marked.append(False)
        
        arr.sort(reverse=True)

        score = 0
        while arr:
            num, index = arr.pop()
            if marked[index] == False:
                score += num
                if index+1 < n: marked[index+1] = True
                if index-1 >= 0: marked[index-1] = True
        
        return score