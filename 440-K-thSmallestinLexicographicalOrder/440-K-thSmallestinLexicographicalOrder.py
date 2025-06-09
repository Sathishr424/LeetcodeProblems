# Last updated: 9/6/2025, 1:56:37 pm
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        def dfs(num):
            if num > n: return
            # print(num)
            for i in range(9 if num == 1 else 10):
                if num <= n:
                    ret.append(num)
                    dfs(num * 10)
                    num += 1
        
        dfs(1)
        return ret