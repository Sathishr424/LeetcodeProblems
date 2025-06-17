# Last updated: 17/6/2025, 8:21:02 pm
@cache
def rec(is_one, index):
    if index == 0: return ['']
    ans = []
    index -= 1
    if is_one:
        curr = rec(False, index)
        for val in curr:
            ans.append('0' + val)
        curr = rec(True, index)
        for val in curr:
            ans.append('1' + val)
    else:
        curr = rec(True, index)
        for val in curr:
            ans.append('1' + val)
    return ans

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ret = []
        
        return rec(True, n)