# Last updated: 12/6/2025, 5:35:27 am

@cache
def fact(x):
    return factorial(x)

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half = ceil(n / 2)

        hash = defaultdict(int)
        ret = 0
        
        start = int(max(0, 10 ** (half-1)))
        end = int(max(9, 10 ** half - 1))

        fact_n = fact(n)
        fact_n_1 = fact(n-1)

        for num in range(start, end+1):
            
            if n % 2 == 0:
                new_num = int(str(num) + str(num)[::-1])
            else:
                new_num = int(str(num) + str(num)[:-1][::-1])
            
            if new_num % k == 0:
                arr = defaultdict(int)
                st = ''.join(sorted(str(new_num)))
                if st in hash: continue
                hash[st] = 1

                while new_num:
                    arr[new_num % 10] += 1
                    new_num //= 10

                bottom = 1
                for char in arr:
                    bottom *= fact(arr[char])
                
                left = fact_n / bottom

                if arr[0]:
                    right = fact_n_1 / (bottom / fact(arr[0]) * fact(arr[0] - 1))
                    ret += left - right
                else:
                    ret += left

        return int(ret)
