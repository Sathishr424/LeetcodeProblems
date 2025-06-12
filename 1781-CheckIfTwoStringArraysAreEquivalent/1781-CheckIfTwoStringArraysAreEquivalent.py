# Last updated: 12/6/2025, 5:40:26 am
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        left = 0
        right = 0
        leftIndex = 0
        rightIndex = 0
        m = len(word1)
        n = len(word2)

        while left < m and right < n:
            if word1[left][leftIndex] != word2[right][rightIndex]: return False
            leftIndex += 1
            rightIndex += 1
            if leftIndex == len(word1[left]):
                leftIndex = 0
                left += 1
            if rightIndex == len(word2[right]):
                rightIndex = 0
                right += 1

        return left == m and right == n
