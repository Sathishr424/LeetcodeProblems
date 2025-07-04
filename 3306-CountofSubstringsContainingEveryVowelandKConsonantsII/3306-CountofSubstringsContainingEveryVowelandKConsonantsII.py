# Last updated: 5/7/2025, 1:38:19 am
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)

        cons = 0
        vowels = defaultdict(int)
        v_cnt = 0
        prev = 0
        prev_2 = 0
        ret = 0

        for i in range(n):
            char = word[i]
            if char in 'aeiou':
                vowels[char] += 1
                if vowels[char] == 1:
                    v_cnt += 1
            else:
                cons += 1
                if cons > k:
                    prev = prev_2
                    while cons > k:
                        char = word[prev]
                        if char in 'aeiou':
                            vowels[char] -= 1
                            if vowels[char] == 0: v_cnt -= 1
                        else:
                            cons -= 1
                        prev += 1
                    prev_2 = prev
            
            if cons == k and v_cnt == 5:
                j = prev_2
                while j < i and word[j] in 'aeiou' and vowels[word[j]] - 1 > 0:
                    vowels[word[j]] -= 1
                    j += 1
                prev_2 = j
            
            if v_cnt == 5 and cons == k:
                ret += prev_2 - prev + 1
        
        return ret