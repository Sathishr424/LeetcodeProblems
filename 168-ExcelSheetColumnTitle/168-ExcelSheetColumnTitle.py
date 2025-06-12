# Last updated: 12/6/2025, 5:52:10 am
alp = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber > 26:
            return self.convertToTitle((columnNumber - 1) // 26) + self.convertToTitle(columnNumber % 26)
        return alp[columnNumber - 1]