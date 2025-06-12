# Last updated: 12/6/2025, 5:46:10 am
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1 if x==0 else 0 for x in i[::-1]] for i in A]
            