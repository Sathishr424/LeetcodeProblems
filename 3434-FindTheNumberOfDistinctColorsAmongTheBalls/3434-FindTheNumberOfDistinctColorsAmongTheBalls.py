# Last updated: 12/6/2025, 5:35:39 am
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_colors = {}
        unique_colors = {}
        ret = []

        for x, y in queries:
            if x in ball_to_colors:
                tmp = ball_to_colors[x]
                unique_colors[tmp] -= 1
                if unique_colors[tmp] == 0:
                    del unique_colors[tmp]
            
            ball_to_colors[x] = y
            if y not in unique_colors:
                unique_colors[y] = 1
            else:
                unique_colors[y] += 1
            ret.append(len(unique_colors))
        return ret
