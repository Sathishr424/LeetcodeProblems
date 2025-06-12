# Last updated: 12/6/2025, 5:47:54 am


class Solution:
    def replaceWords(self, dictionary: List[str], sen: str) -> str:
        hash = set(dictionary)
        ret = ''
        curr = ''
        i = 0
        n = len(sen)
        while i < n:
            if sen[i] == ' ':
                ret += curr + ' '
                curr = ''
            else:
                curr += sen[i]
                if curr in hash:
                    while i < n and sen[i] != ' ': i += 1
                    continue
            i += 1
        ret += curr
        return ret