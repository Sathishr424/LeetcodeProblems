# Last updated: 12/6/2025, 5:36:22 am
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str2)

        index = 0

        for i in range(len(str1)):
            if index < n and (str1[i] == str2[index] or (str1[i] == 'z' and str2[index] == 'a') or ord(str1[i])+1 == ord(str2[index])):
                index += 1
        
        return index == n