# Last updated: 8/9/2025, 11:32:42 am
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if str(i).find('0') == -1 and str(n - i).find('0') == -1:
                return [i, n - i]
