# Last updated: 22/11/2025, 8:42:26 pm
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        left = [int(d) for d in str(num1 - 1)]
        right = [int(d) for d in str(num2)]

        # print(left, right)
        current = left
        n = len(current)

        @cache
        def rec(index, prev_prev, prev, w, strict):
            if index >= n:
                return w
            # print(index, prev_prev, prev, w, strict)
            ans = 0
            if strict:
                for i in range(current[index] + 1):
                    if index > 1 and prev > prev_prev and prev > i:
                        ans += rec(index + 1, prev, i, w + 1, i == current[index])
                    elif index > 1 and  prev < prev_prev and prev < i:
                        ans += rec(index + 1, prev, i, w + 1, i == current[index])
                    else:
                        ans += rec(index + 1, prev, i, w, i == current[index])
            else:
                for i in range(10):
                    if index > 1 and  prev > prev_prev and prev > i:
                        ans += rec(index + 1, prev, i, w + 1, False)
                    elif index > 1 and  prev < prev_prev and prev < i:
                        ans += rec(index + 1, prev, i, w + 1, False)
                    else:
                        ans += rec(index + 1, prev, i, w, False)

            return ans

        @cache
        def rec2(index, prev_prev, prev, w):
            if index >= n - 1:
                return w

            ans = w
            for i in range(10):
                if index > 1 and  prev > prev_prev and prev > i:
                    ans += rec2(index + 1, prev, i, w + 1)
                elif index > 1 and  prev < prev_prev and prev < i:
                    ans += rec2(index + 1, prev, i, w + 1)
                else:
                    ans += rec2(index + 1, prev, i, w)

            return ans

        left_ans = 0
        for i in range(1, current[0] + 1):
            left_ans += rec(1, -1, i, 0, i == current[0])

        # print(left_ans)
        if n > 1:
            for i in range(1, 10):
                left_ans += rec2(1, -1, i, 0)
        # print(left_ans)
        rec.cache_clear()
        rec2.cache_clear()
        current = right
        n = len(current)
            
        right_ans = 0
        for i in range(1, current[0] + 1):
            right_ans += rec(1, -1, i, 0, i == current[0])

        # print(right_ans, 'last before')
        if n > 1:
            for i in range(1, 10):
                right_ans += rec2(1, -1, i, 0)

        # print(right_ans, 'last')
        rec.cache_clear()
        rec2.cache_clear()
        return right_ans - left_ans