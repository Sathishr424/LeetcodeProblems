# Last updated: 12/6/2025, 5:40:35 am
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # TODO
        n = len(s)
        count_a = [0] * n
        count_b = [0] * n
        b_count = 0

        for i in range(n):
            count_b[i] = b_count
            if s[i] == "b":
                b_count += 1

        a_count = 0
        for i in range(n - 1, -1, -1):
            count_a[i] = a_count
            if s[i] == "a":
                a_count += 1

        min_deletions = n
        for i in range(n):
            min_deletions = min(min_deletions, count_a[i] + count_b[i])
        return min_deletions