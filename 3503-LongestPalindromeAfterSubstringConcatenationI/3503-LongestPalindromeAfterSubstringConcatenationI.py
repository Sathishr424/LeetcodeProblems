# Last updated: 27/6/2025, 5:17:18 am
class Solution:
    def primePalindrome(self, n: int) -> int:
        def isPrime(num):
            if num == 1: return False
            if num == 2: return True
            if num == 3: return True

            if num % 2 == 0: return False

            for i in range(3, int(num ** 0.5) + 1, 2):
                if num % i == 0: return False
            
            return True
        
        stack = deque([''])

        while stack:
            num = stack.popleft()
            # print(num, '===>')

            if len(num):
                r_num = int(num + num[::-1])
                # print(r_num)
                if r_num >= n and isPrime(r_num):
                    return r_num
                
            for i in range(10):
                r_num = int(num + str(i) + num[::-1])
                # print(r_num)
                if r_num >= n and isPrime(r_num):
                    return r_num
            
            for i in range(10):
                stack.append(num + str(i))



            