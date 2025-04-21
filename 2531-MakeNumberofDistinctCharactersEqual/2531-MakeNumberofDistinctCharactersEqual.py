# Last updated: 22/4/2025, 1:01:19 am
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

            if x_char in y and x_cnt == y_cnt: return True

            x_cnt -= x[x_char] == 1
            y_cnt += x_char not in y

            for y_char in y:
                if y_char == x_char: continue
                y_ = y_cnt
                x_ = x_cnt
                
                if y[y_char] == 1: y_ -= 1
                if y_char not in x: x_ += 1

                if y_ == x_: return True

        return False