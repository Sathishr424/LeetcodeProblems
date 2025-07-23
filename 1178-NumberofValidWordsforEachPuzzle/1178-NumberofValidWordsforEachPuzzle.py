# Last updated: 23/7/2025, 8:50:07 pm
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        n = len(words)
        m = len(puzzles)

        firstLetters = [defaultdict(int) for _ in range(26)]

        def alpToInt(char):
            return ord(char) - ord('a')

        for word in words:
            uniq = {}
            for char in word:
                uniq[char] = 1
            if len(uniq) > 7: continue
            mask = 0
            for char in uniq:
                mask |= 1 << alpToInt(char)

            for char in uniq:
                firstLetters[alpToInt(char)][mask] += 1
        
        def rec(puzzle, index, first, mask):
            can_add = firstLetters[first][mask]
            ans = 0
            if can_add:
                ans += firstLetters[first][mask]
                firstLetters[first][mask] = 0
            if index < len(puzzle):
                ans += rec(puzzle, index + 1, first, mask)
                ans += rec(puzzle, index + 1, first, mask | (1 << alpToInt(puzzle[index])))
            if can_add:
                firstLetters[first][mask] = can_add
            return ans

        ret = []
        for puzzle in puzzles:
            char = puzzle[0]
            a = alpToInt(char)
            cnt = rec(puzzle, 1, a, 1 << a)
            ret.append(cnt)
        
        return ret