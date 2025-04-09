# Last updated: 9/4/2025, 11:22:11 pm
class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        n = len(num)

        maxi_index = n-1
        maxi_index_final = n-1
        replace_index = -1

        for i in range(n-2, -1, -1):
            if num[i] > num[maxi_index]:
                maxi_index = i
            
            if num[i] != num[maxi_index]:
                replace_index = i
                maxi_index_final = maxi_index

        if replace_index == -1: return int(num)

        return int(num[:replace_index] + num[maxi_index_final] + num[replace_index+1:maxi_index_final] + num[replace_index] + num[maxi_index_final+1:])