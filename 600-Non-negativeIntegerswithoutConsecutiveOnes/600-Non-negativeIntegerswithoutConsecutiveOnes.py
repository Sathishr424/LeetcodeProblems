# Last updated: 5/10/2025, 11:43:31 pm
class Solution:
    def findIntegers(self, n: int) -> int:
        bits = [0] * 32
        m = n.bit_length()

        num = n
        index = 31
        while num:
            bits[index] = num & 1
            num >>= 1
            index -= 1
        index += 1

        @cache
        def rec(index, is_one, strict, add):
            if index == 32:
                return 1
            ans = add
            if strict:
                curr = bits[index]
                ans += rec(index + 1, 0, curr == 0, add)
                if curr and not is_one:
                    ans += rec(index + 1, 1, 1, add)
            else:
                if not is_one:
                    ans += rec(index + 1, 1, 0, add)
                ans += rec(index + 1, 0, 0, add)

            return ans
        
        ans = 1
        ans += rec(index + 1, 1, 1, 0)
        if index + 2 <= 32:
            ans += rec(index + 2, 1, 0, 1)
        rec.cache_clear()
        return ans