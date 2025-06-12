# Last updated: 12/6/2025, 5:45:22 am
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) <= 1: return False
        hash = {}

        for card in deck:
            if card in hash: hash[card] += 1
            else: hash[card] = 1
        
        def gcd(a, b):
            if a == 0: return b; 
            return gcd(b % a, a)
        
        cf = hash[card]

        for k in hash:
            cf = gcd(hash[k], cf)
            if cf == 1: return False

        for k in hash:
            if hash[k] % cf != 0: return False
        return True

        
