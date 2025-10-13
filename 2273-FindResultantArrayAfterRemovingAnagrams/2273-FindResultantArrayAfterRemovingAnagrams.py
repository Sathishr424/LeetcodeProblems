# Last updated: 13/10/2025, 6:32:56 am
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)

        stack = []
        for word in words:
            if stack:
                freq = defaultdict(int)
                for char in word: freq[char] += 1
                for char in stack[-1]:
                    if freq[char] == 0: break
                    freq[char] -= 1
                else:
                    for char in freq:
                        if freq[char]: break
                    else:
                        continue
            stack.append(word)
        
        return stack