# Last updated: 27/6/2025, 1:23:58 am
class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = [0] * 10

        for char in num:
            freq[int(char)] += 1
        
        to_add = []
        odds = []

        for i in range(9, -1, -1):
            cnt = freq[i]
            if freq[i] > 1:
                to_add.append(i)
                cnt %= 2
            
            if freq[i] % 2:
                if len(odds) < 2: odds.append(i)
        
        can_add_zero = True
        if freq[0] > 1 and len(to_add) == 1:
            can_add_zero = False
        
        ret = ''
        for i in to_add:
            if i != 0 or can_add_zero:
                ret = ret + str(i) * (freq[i] // 2)

        if len(odds):
            ret = ret + str(odds[0]) + ret[::-1]
        else:
            ret = ret + ret[::-1]
        
        return ret if len(ret) else '0'