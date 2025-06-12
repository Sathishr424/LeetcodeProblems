# Last updated: 12/6/2025, 5:41:25 am
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        fList = 0
        for i in range(1,n+1):
            if n%i == 0:
                if fList+1 == k: return i
                fList+=1
        return -1