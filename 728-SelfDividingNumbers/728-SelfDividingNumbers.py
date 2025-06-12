# Last updated: 12/6/2025, 5:47:20 am
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ret = []
        for i in range(left, right+1):
            if i % 10 == 0: continue
            num = i
            while num and num % 10 != 0 and i % (num % 10) == 0:
                num //= 10
            if num == 0: ret.append(i)
        return ret