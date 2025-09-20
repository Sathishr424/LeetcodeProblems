# Last updated: 20/9/2025, 7:02:23 pm
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        diff = [0] * (n + 1)

        for start, end, d in shifts:
            val = 1 if d == 1 else -1

            diff[start] += val
            diff[end + 1] -= val

        curr = 0
        final_s = []
        for i in range(n):
            curr += diff[i]
            a = ord(s[i]) - ord('a')
            new_a = (a + curr) % 26
            final_s.append(chr(new_a + ord('a')))

        return ''.join(final_s)