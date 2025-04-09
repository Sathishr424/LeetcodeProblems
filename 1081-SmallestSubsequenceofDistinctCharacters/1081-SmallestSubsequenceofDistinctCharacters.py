# Last updated: 9/4/2025, 9:54:31 pm
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
            while j >= 0 and ret[j] > a and hash[ret[j]] >= 1:
                del his[ret.pop()]
                j -= 1
            ret.append(a)
            his[a] = 1
            hash[a] -= 1

        return "".join(ret)