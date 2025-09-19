# Last updated: 19/9/2025, 7:08:27 pm
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        n = len(rolls)
        
        s = set()
        min_window = 1
        for a in rolls:
            s.add(a)
            if len(s) == k:
                min_window += 1
                s.clear()
        
        return min_window
