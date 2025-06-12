# Last updated: 12/6/2025, 5:37:27 am
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        x = [0] * 26
        y = [0] * 26

        x_uniq = 0
        y_uniq = 0

        for char in word1:
            x[ord(char) - 97] += 1
        
        for char in word2:
            y[ord(char) - 97] += 1

        for i in range(26):
            x_uniq += x[i] > 0
            y_uniq += y[i] > 0

        for x_char in range(26):
            if x[x_char] == 0: continue
            x_cnt = x_uniq
            y_cnt = y_uniq

            if y[x_char] > 0 and x_cnt == y_cnt: return True

            x_cnt -= x[x_char] == 1
            y_cnt += y[x_char] == 0

            for y_char in range(26):
                if y[y_char] == 0: continue
                if y_char == x_char: continue
                y_ = y_cnt
                x_ = x_cnt
                
                if y[y_char] == 1: y_ -= 1
                if x[y_char] == 0: x_ += 1

                if y_ == x_: return True

        return False