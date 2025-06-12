# Last updated: 12/6/2025, 5:55:22 am
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        arr = ['I', 'V', 'X', "L", 'C', 'D', 'M']
        val = [1, 5, 10, 50, 100, 500, 1000]
        hash = {
            'I': 0,
            'V': 1,
            'X': 2,
            'L': 3,
            'C': 4,
            'D': 5,
            'M': 6
        }

        spec = {
            'I': 0, 'X': 0, 'C': 0
        }

        n = len(s)
        i = 0
        while i < n:
            index = hash[s[i]]
            if s[i] in spec and i+1 < n:
                if s[i+1] == arr[index+1]:
                    ans += val[index+1] - val[index]
                    i += 1
                elif s[i+1] == arr[index+2]:
                    ans += val[index+2] - val[index]
                    i += 1
                else:
                    ans += val[index]
            else:
                ans += val[index]
            i += 1

        # "I", 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'
        return ans