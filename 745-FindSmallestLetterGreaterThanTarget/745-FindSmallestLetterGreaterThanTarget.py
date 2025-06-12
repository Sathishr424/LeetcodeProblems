# Last updated: 12/6/2025, 5:47:09 am
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        char = ord(target)

        left = 0
        right = len(letters)-1

        while left < right:
            mid = (left+right)//2

            if ord(letters[mid]) <= char:
                left = mid+1
            else:
                right = mid

        return letters[right] if ord(letters[right]) > char else letters[0]