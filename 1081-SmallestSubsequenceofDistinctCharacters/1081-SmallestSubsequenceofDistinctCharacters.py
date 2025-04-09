# Last updated: 9/4/2025, 9:03:04 pm
alp = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n'
: 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        hash = defaultdict(int)
        for a in s: hash[a] += 1
        ret = []
        his = {}
        for a in s:
            if a in his:
                hash[a] -= 1
                continue
            j = len(ret)-1
            while j >= 0 and alp[ret[j]] > alp[a] and hash[ret[j]] >= 1:
                del his[ret.pop()]
                j -= 1
            ret.append(a)
            his[a] = 1
            hash[a] -= 1

        return "".join(ret)