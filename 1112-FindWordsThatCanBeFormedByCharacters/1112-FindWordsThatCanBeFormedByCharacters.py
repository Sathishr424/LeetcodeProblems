# Last updated: 12/6/2025, 5:44:05 am
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        alp = [0] * 26

        def check(word, index, n):
            if index == n: return n

            val = ord(word[index])-97
            if alp[val]:
                alp[val] -= 1
                ans = check(word, index+1, n)
                alp[val] += 1
                return ans
            return 0

        for c in chars:
            alp[ord(c)-97] += 1

        ret = 0
        for word in words:
            ret += check(word, 0, len(word))
        
        return ret