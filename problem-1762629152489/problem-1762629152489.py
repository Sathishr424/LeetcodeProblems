# Last updated: 9/11/2025, 12:42:32 am
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        n = len(word)
        d = 1
        num = 0
        div = []
        for i in range(n):
            num = (num * 10 % m + int(word[i])) % m
            div.append(1 if num == 0 else 0)

        return div