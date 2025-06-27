# Last updated: 27/6/2025, 5:38:36 am
primes = [2, 3, 5, 7]

@cache
def isPrime(num):
    if num == 1: return False
    if num == 2: return True
    if num == 3: return True

    if num % 2 == 0: return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0: return False
    
    return True

class Solution:
    def primePalindrome(self, n: int) -> int:
        for num in primes:
            if num >= n: return num
        
        def getPalindrome(num):
            r_num = num
            while num:
                r_num = r_num * 10 + (num % 10)
                num //= 10
            return r_num
        
        def getPalindromeExtra(num, extra):
            r_num = num * 10 + extra
            while num:
                r_num = r_num * 10 + (num % 10)
                num //= 10
            return r_num
        
        stack = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

        while stack:
            num = stack.popleft()

            r_num = getPalindrome(num)
            if r_num >= n and isPrime(r_num):
                return r_num

            for i in range(10):
                r_num = getPalindromeExtra(num, i)
                if r_num >= n and isPrime(r_num):
                    return r_num
                stack.append(num * 10 + i)