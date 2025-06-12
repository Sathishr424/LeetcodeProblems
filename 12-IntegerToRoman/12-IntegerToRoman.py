# Last updated: 12/6/2025, 5:55:25 am
class Solution:
    def intToRoman(self, num: int) -> str:
        hash = {
            1: 0,
            5: 1,
            10: 2,
            50: 3,
            100: 4,
            500: 5,
            1000: 6,
        }

        roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        ret = []
        prev = 1

        while num > 0:
            n = num % 10
            curr = n * prev
            num //= 10

            if n == 4:
                index = hash[curr + prev]
                ret.append(roman[index-1] + roman[index])
            elif n == 6:
                index = hash[curr - prev]
                ret.append(roman[index] + roman[index - 1])
            elif n == 9:
                index = hash[curr + prev]
                ret.append(roman[index - 2] + roman[index])
            elif n < 4:
                index = hash[prev]
                ret += roman[index] * n
            elif n >= 5:
                index = hash[prev]
                ret.append(roman[index+1] + (roman[index] * (n-5)))

            prev *= 10

        return ''.join(ret[::-1])


