# Last updated: 17/6/2025, 8:19:43 pm
class Solution:
    def validStrings(self, n: int) -> List[str]:
        ret = []
        
        @cache
        def rec(is_one, index):
            if index == n: return ['']
            ans = []
            if is_one:
                curr = rec(False, index + 1)
                for val in curr:
                    ans.append('0' + val)
                curr = rec(True, index + 1)
                for val in curr:
                    ans.append('1' + val)
            else:
                curr = rec(True, index + 1)
                for val in curr:
                    ans.append('1' + val)
            return ans
        
        return rec(True, 0)