# Last updated: 12/6/2025, 5:42:08 am
alp = list("abcdefghijklmnopqrstuvwxyz")

class Solution:
    def minSort(self,s):
        if len(s) <= 1: return '',s
        ret = ""
        index = -1
        mini = 30
        while True:
            there = False
            for i in range(len(s)):
                if alp.index(s[i]) < mini and s[i] not in list(ret):
                    mini = alp.index(s[i])
                    index = i
                    if not there: there = True
            if not there:
                break
            else:
                ret += alp[mini]
                mini = 30
                s = str(s[:index]) + str(s[index+1:])
        return s,ret
                
        
    def maxSort(self,s):
        if len(s) <= 1: return '',s
        ret = ""
        index = -1
        maxi = -1
        while True:
            there = False
            for i in range(len(s)):
                if alp.index(s[i]) > maxi and s[i] not in list(ret):
                    maxi = alp.index(s[i])
                    index = i
                    if not there: there = True
            if not there:
                break
            else:
                ret += alp[maxi]
                maxi = -1
                s = str(s[:index]) + str(s[index+1:])
        return s,ret
        
    def sortString(self, s: str) -> str:
        ret = ""
        while len(s) > 0:
            s,tmp = self.minSort(s)
            ret += tmp
            print(ret)
            s,tmp = self.maxSort(s)
            ret += tmp
            print(ret)
        return ret
                
        