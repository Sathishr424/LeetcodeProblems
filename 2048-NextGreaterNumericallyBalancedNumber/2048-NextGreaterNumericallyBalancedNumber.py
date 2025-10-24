# Last updated: 24/10/2025, 5:53:27 am
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        num = n + 1
        while True:
            uniq = defaultdict(int)
            tmp = num
            while tmp:
                uniq[tmp % 10] += 1
                tmp //= 10
            
            for i in range(10):
                if uniq[i] == 0: continue
                if uniq[i] != i: break
            else:
                return num
            num += 1
        
