# Last updated: 12/6/2025, 5:35:40 am
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        line_sweep = defaultdict(int)

        for x, y in meetings:
            line_sweep[x] += 1
            line_sweep[y+1] -= 1

        ret = 0
        curr_sum = 0
        prev = 1

        for day in sorted(line_sweep.keys()):
            if curr_sum == 0:
                ret += day-prev
            
            curr_sum += line_sweep[day]
            prev = day
        
        return ret+days-(prev-1)