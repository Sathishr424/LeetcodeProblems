# Last updated: 27/8/2025, 10:15:29 pm
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ret = []
        for col in range(ord(s[0]), ord(s[3]) + 1):
            for row in range(int(s[1]), int(s[4]) + 1):
                ret.append(chr(col) + str(row))

        return ret