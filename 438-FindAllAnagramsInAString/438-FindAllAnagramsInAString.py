# Last updated: 12/6/2025, 5:49:28 am
class customHash:
    def __init__(self, hash):
        self.hash = hash
        self.cnt = len(hash)
        self.balance = 0
    
    def add(self, val, index=-1):
        if val in self.hash:
            self.hash[val] += 1
            if self.hash[val] == 1: self.cnt += 1
            if self.hash[val] == 0: self.balance -= 1
            # print(self.hash, self.cnt, val, index)
            if self.hash[val] == 0:
                return self.balance == 0 and self.cnt == 0
        return False
    
    def reduce(self, val, index=-1):
        if val in self.hash:
            self.hash[val] -= 1
            if self.hash[val] == 0: self.cnt -= 1
            if self.hash[val] == -1: self.balance += 1
            # print(self.hash, self.cnt, val)
            if self.hash[val] == 0:
                return self.balance == 0 and self.cnt == 0
        return False

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = len(p)
        if len(s) < m: return []
        ret = []
        hash = {}
        for i in p:
            if i in hash: hash[i] += 1
            else: hash[i] = 1
        cHash = customHash(hash)

        for i in range(0,m):
            cHash.reduce(s[i])
        # print()
        if cHash.cnt == 0: ret.append(0)
        for i in range(0,len(s)-m):
            cHash.add(s[i], i+1)
            if cHash.reduce(s[i+m], i+m): ret.append(i+1)
            
        return ret
