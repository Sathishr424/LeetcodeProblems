# Last updated: 12/6/2025, 5:48:31 am
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split(" ")])