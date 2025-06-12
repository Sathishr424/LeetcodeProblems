# Last updated: 12/6/2025, 5:48:53 am
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        hash = [{'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1, 'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1}, {'a': 1, 's': 1, 'd': 1, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1}, {'z': 1, 'x': 1, 'c': 1, 'v': 1, 'b': 1, 'n': 1, 'm': 1}]

        ret = []
        for w in words:
            for i in range(3):
                if w[0].lower() in hash[i]:
                    there = 1
                    for j in range(1, len(w)):
                        if w[j].lower() not in hash[i]:
                            there = 0
                            break
                    if there: ret.append(w)
                    break
        return ret