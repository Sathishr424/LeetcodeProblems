# Last updated: 11/5/2025, 6:17:46 pm
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        freq = [0] * 26

        arr = [ord(char) - 97 for char in s]
        ret = 0

        left = [0] * 26
        right = [0] * 26
        
        for i in range(1, n):
            right[arr[i]] += 1
        
        left[arr[0]] += 1

        visited = [[1] * 26 for _ in range(26)]
        
        for i in range(1, n):
            a = arr[i]
            right[a] -= 1

            for num in range(26):
                if visited[num][a] and left[num] and right[num]:
                    ret += 1
                    visited[num][a] = 0
            
            left[a] += 1
        
        return ret
            
