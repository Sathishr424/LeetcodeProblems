# Last updated: 14/4/2025, 8:48:04 pm
class Solution:
    def getPermutation(self, n: int, k: int) -> str:

        def fact(num):
            if num < 3:
                return num
            return fact(num - 1) * num

        s = []
        k -= 1
        val = [str(i) for i in range(1, n + 1)]
        while n > 1:
            curid = k // fact(n - 1)
            curval = val[curid]
            val.remove(curval)
            s.append(curval)
            k -= (fact(n - 1) * curid)
            n -= 1
        s.append(val[0])
        return "".join(s)
        