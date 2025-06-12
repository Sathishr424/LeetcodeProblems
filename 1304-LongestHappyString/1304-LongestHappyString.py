# Last updated: 12/6/2025, 5:42:59 am
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        abc = [[a, 'a'], [b, 'b'], [c, 'c']]
        abc.sort(reverse=True, key=lambda x: x[0])
        index = 0
        st = ''
        while True:
            if abc[0][0] == 0: break
            if len(st) > 0 and abc[index][1] == st[-1]: 
                index += 1
                if abc[index][0] == 0: break
            val = min(abs(index * -3 + 2), abc[index][0])
            st += abc[index][1] * val
            abc[index][0] -= val
            abc.sort(reverse=True, key=lambda x: x[0])
            index = 0
        return st