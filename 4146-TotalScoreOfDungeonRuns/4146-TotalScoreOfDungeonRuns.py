# Last updated: 12/25/2025, 7:07:55 PM
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)

        rem = hp
        sl = SortedList()

        for i in range(n):
            rem -= damage[i]
            need = max(0, requirement[i] - rem)
            sl.add(need)

        points = sl.bisect_right(0)
        rem = hp
        left = 0
        for i in range(1, n):
            left += damage[i - 1]
            rem -= damage[i - 1]
            need = max(0, requirement[i - 1] - rem)
            sl.remove(need)
            
            curr = sl.bisect_right(left)
            points += curr
            # print(i, curr)
            
        return points