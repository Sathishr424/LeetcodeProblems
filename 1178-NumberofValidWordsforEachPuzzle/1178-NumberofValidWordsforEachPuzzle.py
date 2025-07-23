# Last updated: 23/7/2025, 9:00:08 pm
@cache
def alpToInt(char):
    return ord(char) - ord('a')

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        firstLetters = [defaultdict(int) for _ in range(26)]

        for word in words:
            uniq = set(word)
            if len(uniq) > 7: continue
            mask = 0
            for char in uniq:
                mask |= 1 << alpToInt(char)

            for char in uniq:
                firstLetters[alpToInt(char)][mask] += 1
        
        def rec(puzzle, index, first, mask):
            if index == len(puzzle):
                if mask in firstLetters[first]:
                    return firstLetters[first][mask]
                return 0
        
            ans = rec(puzzle, index + 1, first, mask)
            ans += rec(puzzle, index + 1, first, mask | (1 << alpToInt(puzzle[index])))
            return ans

        ret = []
        for puzzle in puzzles:
            char = puzzle[0]
            a = alpToInt(char)
            cnt = rec(puzzle, 1, a, 1 << a)
            ret.append(cnt)
        
        return ret