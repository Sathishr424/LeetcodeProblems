# Last updated: 12/4/2025, 6:53:32 pm
from collections import defaultdict
from math import ceil, factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = ceil(n / 2)

        start = 10 ** (half-1)
        end = 10 ** half - 1

        hash = defaultdict(int)

        def reverseNum(num):
            rev = 0

            if n % 2 == 1:
                num //= 10
            
            while num:
                rev = rev * 10 + (num % 10)
                num //= 10
            
            return rev

        ret = 0
        
        @cache
        def fact(x):
            return factorial(x)
        
        start = int(max(0, start))
        end = int(max(9, end))
        to_add = 10 ** (n//2)

        for num in range(start, end+1):
            
            new_num = num * to_add + reverseNum(num)
            
            if new_num % k == 0:
                arr = defaultdict(int)
                arr_2 = []

                while new_num:
                    arr_2.append(new_num % 10)
                    arr[new_num % 10] += 1
                    new_num //= 10
                
                st = ''.join([str(c) for c in sorted(arr_2)])

                if st in hash: continue
                hash[st] = 1

                bottom = 1
                for char in arr:
                    bottom *= factorial(arr[char])
                
                left = fact(n) / bottom

                if arr[0]:
                    right = fact(n-1) / (bottom / fact(arr[0]) * fact(arr[0] - 1))
                    ret += left - right
                else:
                    ret += left

        return int(ret)
