# Last updated: 12/6/2025, 5:42:13 am
class Solution:
    def numberOfSubstrings(self, word: str) -> int:
        n = len(word)
        ret = 0
        def to_match(char):
            return 0 if char == 'a' else 1 if char == 'b' else 2

        matches = 0
        curr = [0, 0, 0]
        valid_start = 0

        for i in range(n):
            index = to_match(word[i])
            curr[index] += 1

            if curr[index] == 1:
                matches += 1
                while matches == 3:
                    ret += n-i
                    index = to_match(word[valid_start])

                    curr[index] -= 1
                    if curr[index] == 0:
                        matches -= 1
                    valid_start += 1
        
        return ret
        