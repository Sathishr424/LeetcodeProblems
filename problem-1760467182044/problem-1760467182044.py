# Last updated: 15/10/2025, 12:09:42 am
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        s = 0
        is_pos = True
        for d in str(n):
            if is_pos:
                s += int(d)
            else:
                s -= int(d)
            is_pos = not is_pos

        return s