# Last updated: 22/4/2025, 12:59:08 am
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        m = len(word1)
        n = len(word2)

        x = defaultdict(int)
        y = defaultdict(int)

        for char in word1:
            x[char] += 1
        
        for char in word2:
            y[char] += 1

        x_uniq = len(x)
        y_uniq = len(y)

        for x_char in x:
            x_cnt = x_uniq
            y_cnt = y_uniq

            if x[x_char] == 1: x_cnt -= 1
            if x_char not in y: y_cnt += 1

            for y_char in y:
                y_ = y_cnt
                x_ = x_cnt

                if y_char == x_char:
                    if y_ == x_+(x[x_char] == 1): return True
                    continue
                
                if y[y_char] == 1: y_ -= 1
                if y_char not in x: x_ += 1

                if y_ == x_: return True

        return False