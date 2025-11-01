# Last updated: 1/11/2025, 11:53:30 pm
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return factorial(n + 4) // (factorial(4) * factorial(n))