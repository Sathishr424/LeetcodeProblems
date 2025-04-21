# Last updated: 22/4/2025, 1:02:54 am
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        x = defaultdict(int)
        y = defaultdict(int)

        for char in word1:
            x[char] += 1
        
        for char in word2:
            y[char] += 1

        for x_char in x:
            x_cnt = len(x)
            y_cnt = len(y)

            if x_char in y and x_cnt == y_cnt: return True

            x_cnt -= x[x_char] == 1
            y_cnt += x_char not in y

            for y_char in y:
                if y_char == x_char: continue
                if y_cnt - (y[y_char] == 1) == x_cnt + (y_char not in x): return True

        return False