# Last updated: 12/6/2025, 5:38:43 am
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ret = 0
        prev = 0
        for row in bank:
            curr = 0
            for floor in row:
                curr += floor == '1'
            if curr != 0:
                ret += prev * curr
                prev = curr
        return ret