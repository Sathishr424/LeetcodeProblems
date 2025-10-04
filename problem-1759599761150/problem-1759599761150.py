# Last updated: 4/10/2025, 11:12:41 pm
class Solution:
    def captureForts(self, forts: List[int]) -> int:
        n = len(forts)

        # 1, 1, 0, 0, -1

        is_command = -1
        is_empty = -1
        best = 0
        for i in range(n):
            if forts[i] == 1:
                if is_empty != -1:
                    best = max(best, i - is_empty - 1)
                is_empty = -1
                is_command = i
            elif forts[i] == -1:
                if is_command != -1:
                    best = max(best, i - is_command - 1)
                is_empty = i
                is_command = -1

        return best