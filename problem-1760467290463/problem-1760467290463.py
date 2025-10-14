# Last updated: 15/10/2025, 12:11:30 am
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        m = len(score)
        n = len(score[0])

        score.sort(key=lambda x: -x[k])
        return score