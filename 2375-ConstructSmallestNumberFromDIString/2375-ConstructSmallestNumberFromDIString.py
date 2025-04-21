# Last updated: 21/4/2025, 5:57:15 pm
class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)

        l = 1
        r = n+1
        vis = [True] * (r+1)
        max_ans = '9' * r

        def rec(index, st):
            if index == r: return st
            ans = max_ans
            if pattern[index-1] == 'I':
                for i in range(int(st[-1])+1, r+1):
                    if vis[i]:
                        vis[i] = False
                        ans = min(ans, rec(index+1, st+str(i)))
                        vis[i] = True
            else:
                for i in range(1, int(st[-1])):
                    if vis[i]:
                        vis[i] = False
                        ans = min(ans, rec(index+1, st+str(i)))
                        vis[i] = True
            return ans
        
        ans = max_ans
        for i in range(1, r+1):
            vis[i] = False
            ans = min(ans, rec(1, str(i)))
            vis[i] = True
        return ans