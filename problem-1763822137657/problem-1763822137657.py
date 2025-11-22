# Last updated: 22/11/2025, 8:05:37 pm
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans = 0
        for num in range(num1, num2+1):
            num = str(num)
            w = 0
            for i in range(1, len(num) - 1):
                if num[i] > num[i-1] and num[i] > num[i + 1]:
                    w += 1
                elif num[i] < num[i-1] and num[i] < num[i + 1]:
                    w += 1
            ans += w

        return ans