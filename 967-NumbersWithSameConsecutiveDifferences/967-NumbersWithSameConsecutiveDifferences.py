# Last updated: 11/7/2025, 9:53:31 pm
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        stack = deque([(i, 1) for i in range(10)])
        end = 10 ** (n - 1)
        ret = []
        while stack:
            num, cnt = stack.popleft()

            if cnt == n:
                if num // end != 0:
                    ret.append(num)
                continue
            
            last = num % 10
            
            add = last + k
            minus = last - k

            if add < 10:
                stack.append((num * 10 + add, cnt + 1))
            if add != minus and minus >= 0:
                stack.append((num * 10 + minus, cnt + 1))

        return ret