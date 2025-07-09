# Last updated: 9/7/2025, 8:23:04 pm
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)

        first = -1
        second = -1
        prev = s[0]
        prev_index = 0
        ret = 0

        ones = [0]
        if s[0] == '1':
            ones.append(1)
        else:
            ones.append(0)

        for i in range(1, n):
            if s[i] == '1':
                ones.append(ones[-1] + 1)
            else:
                ones.append(ones[-1])
            
            if s[i] != prev:
                if prev == '0':
                    if first == -1:
                        first = prev_index
                    else:
                        first = second
                        second = prev_index
                elif first != -1:
                    second = i
                        
                prev = s[i]
                prev_index = i
        
            if s[i] == '0' and first != -1 and second != -1:
                dis = i - first + 1
                dis -= ones[-1] - ones[first]
                ret = max(ret, dis)

        return ret + ones[-1]
