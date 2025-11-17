# Last updated: 18/11/2025, 1:29:41 am
class Solution:
    def splitNum(self, num: int) -> int:
        arr = [int(d) for d in str(num)]

        arr.sort(reverse=True)

        a = 0
        b = 0
        while len(arr) > 1:
            a = a * 10 + arr.pop()
            b = b * 10 + arr.pop()

        if arr:
            a = a * 10 + arr.pop()

        return a + b
        