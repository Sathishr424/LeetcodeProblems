# Last updated: 12/6/2025, 5:55:34 am
import re

nums = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

class Solution:
    def myAtoi(self, s: str) -> int:
        s = re.sub('^ +', '', s)
        if len(s) <= 0 or s[0] == '.': return 0
        t = 'none'
        index = 0
        if s[index] == '-' or s[index] == '+':
            t = s[0]
            index += 1
            if index >= len(s): return 0
        s = s[:index] + re.sub("^0+", "", s[index:])
        if len(s) < 1: return 0
        if s[index] not in nums: return 0
        dig = 0
        for i in range(index, len(s)):
            if s[i] in nums:
                dig = (dig * 10) + nums[s[i]]
            else:
                break
        if dig > 2147483647 and t == '-': dig = 2147483648
        elif dig > 2147483647: dig = 2147483647
        return -dig if t == '-' else dig
            