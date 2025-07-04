# Last updated: 5/7/2025, 12:48:22 am
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # a, aa, aabb
        # a, aa, aaaa
        
        # aa, aabb, aabbaabb, aabbaabb bbccbbcc
        # 10 -> 5 -> 
        # 8 -> 4 -> 2 -> 1
        num = 1
        power = 0
        curr = 'a'
        while num * 2 <= k:
            num *= 2
            if operations[power] == 1:
                curr = chr((ord(curr) - ord('a') + 1) % 26 + ord('a'))
            power += 1
        
        rem = k - num
        if rem:
            curr = self.kthCharacter(rem, operations)
            if operations[power] == 1:
                curr = chr((ord(curr) - ord('a') + 1) % 26 + ord('a'))
                return curr
        return curr