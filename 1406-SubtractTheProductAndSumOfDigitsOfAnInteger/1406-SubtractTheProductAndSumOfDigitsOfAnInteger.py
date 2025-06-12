# Last updated: 12/6/2025, 5:42:36 am
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1; sm = 0;
        for i in str(n):
            product *= int(i); sm += int(i);
        return product - sm