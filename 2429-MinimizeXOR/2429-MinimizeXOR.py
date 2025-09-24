# Last updated: 24/9/2025, 11:23:01 pm
class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bit_cnt = num2.bit_count()

        bits = [0] * 32
        index = 0
        while num1:
            bits[index] = num1 & 1
            num1 >>= 1
            index += 1

        num = 0
        for i in range(31, -1, -1):
            if bits[i] and bit_cnt:
                num += 1 << i
                bit_cnt -= 1

        index = 0
        while bit_cnt:
            if num & (1 << index) == 0:
                num += 1 << index
                bit_cnt -= 1

            index += 1

        return num