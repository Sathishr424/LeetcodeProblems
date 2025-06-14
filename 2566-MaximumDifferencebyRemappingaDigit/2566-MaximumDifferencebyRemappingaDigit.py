# Last updated: 14/6/2025, 11:21:18 am
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        n = len(num)

        i = 0
        while i < n and num[i] == '9':
            i += 1
        
        maxi = num[:i]
        for j in range(i, n):
            if num[j] == num[i]:
                maxi += '9'
            else:
                maxi += num[j]
        
        mini = ''
        for i in range(n):
            if num[i] == num[0]:
                mini += '0'
            else:
                mini += num[i]

        return int(maxi) - int(mini)