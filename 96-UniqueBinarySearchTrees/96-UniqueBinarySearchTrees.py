# Last updated: 5/8/2025, 11:12:33 am
fact = [1] * 34

for i in range(1, 34):
    fact[i] = fact[i - 1] * i

class Solution:
    def getRow(self, row: int) -> List[int]:
        ret = []
        for i in range(row + 1):
            ret.append(fact[row] // (fact[i] * fact[row - i]))
        
        return ret