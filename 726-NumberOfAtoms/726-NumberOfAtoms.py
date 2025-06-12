# Last updated: 12/6/2025, 5:47:22 am
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)

        def sub(l, r):
            curr = ''
            currType = 0
            cnt = 0
            hsh = defaultdict(int)

            def calculate():
                if curr:
                    if currType:
                        for f in curr: 
                            if f in hsh: hsh[f] += curr[f] * cnt
                            else: hsh[f] = curr[f] * cnt
                    else: hsh[curr] += cnt

            while l <= r:
                if formula[l] == '(':
                    calculate()
                    i = l+1
                    open = 1
                    while i <= r:
                        if formula[i] == '(': open += 1
                        elif formula[i] == ')':
                            if open == 1: break 
                            open -= 1
                        i += 1
                    curr = sub(l+1, i-1)
                    currType = 1
                    cnt = 1
                    l = i
                elif formula[l].isdigit():
                    if not formula[l-1].isdigit(): cnt = 0
                    cnt = cnt * 10 + int(formula[l])
                elif formula[l] == formula[l].upper():
                    calculate()
                    curr = formula[l]
                    cnt = 1
                    currType = 0
                else:
                    curr += formula[l]
                l += 1
            calculate()
            return hsh
        hsh = sub(0, n-1)
        ret = ''
        for k in sorted(list(hsh.keys())):
            ret += f"{k}{hsh[k] if hsh[k] > 1 else ''}"
        return ret
                            
