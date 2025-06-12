# Last updated: 12/6/2025, 5:46:24 am
class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        curr = 0
        for c in s:
            width = widths[ord(c)-97]
            if curr+width <= 100:
                curr += width
            else:
                lines += 1
                curr = width
        return [lines, curr]