# Last updated: 12/6/2025, 5:39:08 am
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        n = len(seats)
        
        ret = 0

        for i in range(n):
            ret += abs(seats[i] - students[i])

        return ret