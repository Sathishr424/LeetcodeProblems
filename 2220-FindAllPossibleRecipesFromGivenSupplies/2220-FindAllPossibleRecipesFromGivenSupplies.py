# Last updated: 12/6/2025, 5:38:50 am
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], s: List[str]) -> List[str]:
        graph = {}
        supplies = {}

        for sup in s: supplies[sup] = 1

        for i in range(len(recipes)):
            graph[recipes[i]] = ingredients[i]

        def dfs(r, vis):
            if r in supplies: return True
            if r in vis: return False

            vis[r] = 1
            
            for ing in graph[r]:
                if ing not in supplies and (ing not in graph or not dfs(ing, vis)): return False
            
            supplies[r] = 1
            return True
        
        ret = []

        for r in recipes:
            if dfs(r, {}): ret.append(r)
        
        return ret

