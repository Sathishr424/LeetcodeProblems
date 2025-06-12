# Last updated: 12/6/2025, 5:47:06 am
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        hash = {}
        for w in licensePlate.lower():
            if ord(w) < 97 or ord(w) > 122: continue
            if w in hash: hash[w] += 1
            else: hash[w] = 1

        total = len(hash)
        prev = float('inf')
        word = None

        for w in words:
            cnt = 0
            tmp = {}
            for c in w:
                if c in hash:
                    if c in tmp:
                        if tmp[c] == hash[c]: continue
                        tmp[c] += 1
                    else: tmp[c] = 1
                    if tmp[c] == hash[c]: cnt += 1

            if cnt == total and len(w) < prev:
                prev = len(w)
                word = w
        return word
                