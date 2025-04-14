# Last updated: 14/4/2025, 5:23:32 pm
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        1, 2, 3
        1, 2, 3, 4, 5
        1, 2, 3, 4
        1, 2, 4, 3

        1, 2, 4, 3, 5, 6
        
        1, 2, 4, 5, 3, 6
        1, 2, 4, 5, 6, 3
        1, 2, 4, 6, 3, 5

        1, 2, 4, 6, 5, 3
        1, 2, 7, 6, 5, 3


        1, 2, 5, 3, 4, 6
        1, 2, 5, 6, 4, 3

        3, 2, 1
        1, 2, 3
        2,1,3


        2,6,7,8,9
        2,6,7,9,8
        2,6,8,9,7

        6,2,7,8,9
        6,2,8,7,9

        6,2,8,7,9
        6,2,8,9,7
        6,2,9,7,8
        6,2,9,8,7

        n = len(nums)

        1, 2, 4, 6, 5, 3
        1,2,5,6,4,3

        1, 2, 7, 6, 5, 3

        1, 3, 7, 6, 5, 2
        start = 0
        end = n-1

        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                for j in range(n-1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        start = i+1
                        break
                break
        
        for k in range(start, (start+end)//2 + 1):
            nums[k], nums[end] = nums[end], nums[k]
            end -= 1
                        
        

        