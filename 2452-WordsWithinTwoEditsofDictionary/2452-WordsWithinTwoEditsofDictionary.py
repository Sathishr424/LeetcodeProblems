# Last updated: 26/9/2025, 2:18:13 am
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries)
        m = len(queries[0])
        there = set()
        
        for word in dictionary:
            there.add(word)
            for i in range(m):
                w = word[:i] + '*' + word[i+1:]
                there.add(w)
                for j in range(i+1, m):
                    w = word[:i] + '*' + word[i+1:j] + '*' + word[j+1:]
                    there.add(w)
        ret = []
        for word in queries:
            if word in there:
                ret.append(word)
                continue

            for i in range(m):
                w = word[:i] + '*' + word[i+1:]
                if w in there:
                    ret.append(word)
                    break
                match = False
                for j in range(i+1, m):
                    w = word[:i] + '*' + word[i+1:j] + '*' + word[j+1:]
                    if w in there:
                        match = True
                        ret.append(word)
                        break
                if match: break

        return ret
                    