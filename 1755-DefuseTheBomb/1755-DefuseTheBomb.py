# Last updated: 12/6/2025, 5:40:36 am
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0: return [0] * n
        sum = 0
        neg = k < 0
        if k < 0: k *= -1
        if neg: code = code[::-1]
        code += code
        for i in range(k):
            sum += code[i]
        ret = []
        for i in range(k, n+k):
            sum = sum - code[i-k] + code[i]
            ret.append(sum)
        if neg: return ret[::-1]
        return ret
