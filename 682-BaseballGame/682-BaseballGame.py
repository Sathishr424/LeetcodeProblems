# Last updated: 12/6/2025, 5:47:42 am
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for o in operations:
            if o == '+':
                arr.append(arr[-1] + arr[-2])
            elif o == 'C':
                arr.pop()
            elif o == 'D':
                arr.append(arr[-1] * 2)
            else:
                arr.append(int(o))
        return sum(arr)