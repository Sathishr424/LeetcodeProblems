# Last updated: 12/6/2025, 5:54:40 am
@cache
def countAndSayHelper(n):
    if n == 1: return '1'

    before = countAndSayHelper(n-1)
    prev = before[0]
    cnt = 1
    ret = ''
    for i in range(1, len(before)):
        if before[i] == prev:
            cnt += 1
        else:
            ret += f"{cnt}{prev}"
            cnt = 1
        prev = before[i]
            
    ret += f"{cnt}{prev}"
    return ret

class Solution:
    def countAndSay(self, n: int) -> str:
        return countAndSayHelper(n)