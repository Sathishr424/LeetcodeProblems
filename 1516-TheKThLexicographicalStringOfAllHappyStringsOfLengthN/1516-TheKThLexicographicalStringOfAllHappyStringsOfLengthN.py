# Last updated: 12/6/2025, 5:41:52 am
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        arr = ['a', 'b', 'c']
        ret = []
        def rec(st):
            if len(ret) == k: return
            if len(st) == n:
                ret.append(st)
                return
            for i in range(3):
                if len(st) == 0 or arr[i] != st[-1]:
                    rec(st + arr[i])

        rec('')

        if len(ret) == k: return ret[-1]
        return ''