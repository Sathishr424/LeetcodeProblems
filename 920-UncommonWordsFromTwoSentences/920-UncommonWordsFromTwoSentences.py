# Last updated: 12/6/2025, 5:45:39 am
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hash = defaultdict(int)
        prev = 0

        def check(st):
            def helper(word):
                hash[word] += 1
                return ""
            curr = ""
            for w in st:
                if w == ' ': curr = helper(curr)
                else: curr += w
            curr = helper(curr)

        check(s1 + " " + s2)
        ret = []
        for k in hash:
            if hash[k] == 1: ret.append(k)
        return ret
