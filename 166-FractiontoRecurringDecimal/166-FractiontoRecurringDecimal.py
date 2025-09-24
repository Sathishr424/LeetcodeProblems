# Last updated: 24/9/2025, 1:29:57 pm
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = 1
        if numerator < 0:
            numerator *= -1
            neg *= -1
        if denominator < 0:
            denominator *= -1
            neg *= -1

        ans = str(numerator // denominator)
        numerator = (numerator % denominator) * 10
        if numerator == 0:
            return '-' + ans if neg == -1 and ans != '0' else ans

        ans += '.'
        seen = {}
        index = len(ans)
        while numerator > 0:
            curr = str(numerator // denominator)
            if numerator in seen:
                index = seen[numerator]
                ans = ans[:index] + '(' + ans[index:] + ')'
                break
            seen[numerator] = index
            ans += curr
            numerator = (numerator % denominator) * 10
            index += 1

        return '-' + ans if neg == -1 and ans != '0' else ans