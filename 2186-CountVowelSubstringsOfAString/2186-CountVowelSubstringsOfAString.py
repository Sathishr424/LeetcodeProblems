# Last updated: 12/6/2025, 5:38:57 am
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        n = len(word)
        ret = 0
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

        matches = 0
        curr = [0, 0, 0, 0, 0]
        ret = 0
        valid_start = 0
        i = 0

        while i < n:
            char = word[i]

            if char in vowels:
                index = vowels[char]
                curr[index] += 1

                if curr[index] == 1:
                    matches += 1
                    if matches == 5:
                        j = i+1
                        while j < n and word[j] in vowels:
                            j += 1
                        cnt = j-i
                        
                        while matches == 5:
                            ret += cnt
                            index = vowels[word[valid_start]]

                            curr[index] -= 1
                            if curr[index] == 0:
                                matches -= 1
                            valid_start += 1
            else:
                curr = [0, 0, 0, 0, 0]
                matches = 0
                valid_start = i+1

            i += 1
        
        return ret