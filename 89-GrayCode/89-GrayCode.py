# Last updated: 12/6/2025, 5:53:33 am
class Solution:
    def grayCode(self, n: int) -> List[int]:
        maxi = 2**n

        val = '0' * (len(bin(maxi))-3)
        stack = deque([val])
        memo = {}
        memo[int(val)] = 1
        ret = []

        while stack:
            st = stack.popleft()
            ret.append(st)

            for i in range(len(st)):
                val = st[:i] + str(int(st[i] == '0')) + st[i+1:]
                integer = int(val)
                if integer not in memo:
                    stack.append(val)
                    memo[integer] = 1
                    break
        return [int(a, 2) for a in ret]