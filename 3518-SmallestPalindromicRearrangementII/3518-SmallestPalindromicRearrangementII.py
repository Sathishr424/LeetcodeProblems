# Last updated: 20/4/2025, 1:07:50 am
@cache
def fact(x):
    if x <= 1: return 1
    return fact(x-1) * x

MAX = 10**6
log_fact = [0] * (MAX+1)
for i in range(1, MAX+1): 
    log_fact[i] = log_fact[i-1] + log2(i)
# print(log_fact)
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        uniq = defaultdict(int)
        for char in s:
            uniq[char] += 1
        
        odd = ''
        half = n//2
        counts = {}

        def getPerm(arr, k, b):
            n = len(arr)
            if n == 0: return ''

            f = log_fact[n]

            for char in counts:
                f -= log_fact[counts[char]]
            
            if f >= 32:
                x = b // fact(counts[arr[0]]) * fact(counts[arr[0]]-1)
                counts[arr[0]] -= 1
                return arr[0] + getPerm(arr[1:], k, x)

            for i in range(n):
                if i > 0 and arr[i] == arr[i-1]: continue
                char = arr[i]

                x = b // fact(counts[char]) * fact(counts[char]-1)
                f = fact(n-1) // x

                if f >= k:
                    counts[char] -= 1
                    return char + getPerm(arr[:i] + arr[i+1:], k, x)

                k -= f
            return ''
        
        bottom = 1
        for char in uniq:
            if uniq[char] % 2:
                odd = char
            counts[char] = uniq[char] // 2
            bottom *= fact(counts[char])

        arr = []
        for char in sorted(counts.keys()):
            for i in range(counts[char]):
                arr.append(char)

        st = getPerm(arr, k, bottom)
        if len(st) != half: return ''
        
        return st + odd + st[::-1]