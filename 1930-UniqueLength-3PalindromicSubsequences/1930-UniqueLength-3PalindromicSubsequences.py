# Last updated: 11/5/2025, 6:08:03 pm
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
        for i in range(1, n-1):
            right[arr[i]] -= 1

            for num in range(26):
                if visited[num][arr[i]] and left[num] * right[num]:
                    ret += 1
                    visited[num][arr[i]] = 0
            
            left[arr[i]] += 1
        
        return ret
            
