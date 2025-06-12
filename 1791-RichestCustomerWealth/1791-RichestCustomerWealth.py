# Last updated: 12/6/2025, 5:40:21 am
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ret = 0
        for i in range(len(accounts)):
            tmp = 0
            for j in range(len(accounts[i])):
                tmp+=accounts[i][j]
            if tmp > ret: ret = tmp
        return ret