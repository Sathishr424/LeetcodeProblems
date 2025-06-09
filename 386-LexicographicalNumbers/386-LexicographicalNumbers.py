# Last updated: 9/6/2025, 8:48:50 pm
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        def dfs(curr):
            if curr > n: return
            for i in range(10):
                new_num = curr + i
                if new_num > n: break
                ret.append(new_num)
                dfs(new_num * 10)
        
        for i in range(1, 10):
            if i > n: break
            ret.append(i)
            dfs(i * 10)
        return ret