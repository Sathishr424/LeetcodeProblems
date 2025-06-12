# Last updated: 12/6/2025, 5:39:51 am
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0]: return edges[0][0]
        elif edges[0][0] == edges[1][1]: return edges[0][0]
        elif edges[0][1] == edges[1][0]: return edges[0][1]
        elif edges[0][1] == edges[1][1]: return edges[0][1]
        