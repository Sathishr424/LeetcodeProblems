# Last updated: 21/6/2025, 6:39:40 pm
ugly = [1]
i = 0
j = 0
k = 0

while 1690 > len(ugly):
    num = min(ugly[i] * 2, ugly[j] * 3, ugly[k] * 5)
    ugly.append(num)
    if num == ugly[i] * 2:
        i += 1
    if num == ugly[j] * 3:
        j += 1
    if num == ugly[k] * 5:
        k += 1

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        return ugly[n-1]
