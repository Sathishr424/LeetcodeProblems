# Last updated: 12/25/2025, 7:10:41 PM
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ret = {}
        n = len(code)

        valid = ["electronics", "grocery", "pharmacy", "restaurant"]
        for v in valid:
            ret[v] = []
        
        for i in range(n):
            c = code[i]
            b = businessLine[i]
            active = isActive[i]

            if not active or b not in valid or len(c) == 0: continue
            okay = True
            for char in c:
                is_valid = char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                is_valid = is_valid or char in '0123456789'
                is_valid = is_valid or char == '_'

                if not is_valid:
                    okay = False
                    break

            if okay: ret[b].append(c)

        ans = []
        for b in valid:
            ans += sorted(ret[b])

        return ans

            