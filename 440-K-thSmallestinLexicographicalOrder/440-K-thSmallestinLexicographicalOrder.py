# Last updated: 9/6/2025, 2:04:53 pm
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        def dfs(num):
            if num > n: return
            for i in range(10):
                if num <= n:
                    ret.append(num)
                    dfs(num * 10)
                    num += 1
        
        for num in range(1, 10):
            if num > n: break
            ret.append(num)
            dfs(num * 10)
        
        return ret