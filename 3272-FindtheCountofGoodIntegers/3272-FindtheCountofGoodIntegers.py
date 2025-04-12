# Last updated: 12/4/2025, 6:21:56 pm
from collections import defaultdict
from math import ceil, factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = ceil(n / 2)

        start = 10 ** (half-1)
        end = 10 ** half - 1

        final = 10 ** n - 1

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
        
        start = int(max(0, start))
        end = int(max(9, end))
        to_add = 10 ** (n//2)

        for num in range(start, end+1):
            
            if n > 1:
                new_num = num * to_add + reverseNum(num)
            else:
                new_num = num
            
            if new_num % k == 0:
                arr = defaultdict(int)
                arr_2 = []
                tmp = new_num
                while new_num:
                    arr_2.append(new_num % 10)
                    arr[new_num % 10] += 1
                    new_num //= 10
                
                st = ''.join([str(c) for c in sorted(arr_2)])

                if st in hash: continue
                hash[st] = 1
                bottom = 1
                cnt = 0
                for char in arr:
                    cnt += arr[char]
                    bottom *= factorial(arr[char])
                
                left = factorial(n) / bottom
                right = 0
                
                if arr[0]:
                    right = factorial(n-1) / (bottom / factorial(arr[0]) * factorial(arr[0] - 1))
                
                ans = left - right
                ret += ans

        return int(ret)
