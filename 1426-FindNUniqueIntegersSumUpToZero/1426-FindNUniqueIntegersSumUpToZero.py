# Last updated: 12/6/2025, 5:42:27 am
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2 == 0:
            return [-i for i in range(1,int(n/2)+1)] + [i for i in range(1,int(n/2)+1)]
        else:
            return [-i for i in range(1,int(n/2)+1)] + [0] + [i for i in range(1,int(n/2)+1)]