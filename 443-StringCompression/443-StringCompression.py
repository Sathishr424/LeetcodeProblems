# Last updated: 12/6/2025, 5:49:23 am
class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        curr = chars[0]
        cnt = 1

        def helper():
            nonlocal cnt, curr, index
            if cnt > 1:
                chars[index] = curr
                tmp = len(str(cnt))
                bu = tmp
                while cnt:
                    rem = cnt % 10
                    cnt //= 10
                    chars[index + tmp] = str(rem)
                    tmp -= 1
                index += bu + 1
                cnt = 1
            else:
                chars[index] = str(curr)
                index += 1

        for i in range(1, len(chars)):
            if chars[i] == curr: cnt += 1
            else: 
                helper()
                curr = chars[i]

        helper()

        return index