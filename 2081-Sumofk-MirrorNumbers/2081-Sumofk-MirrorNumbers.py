# Last updated: 23/6/2025, 12:02:57 pm
def is_palindrome(num):
    st = str(num)
    return st == st[::-1]

def getPalBaseNum(num, pal, base):
    while pal:
        rem = pal % 10
        num = num * base + rem
        pal //= 10
    return num

p = [[0] * 31 for _ in range(10)]
for k in range(2, 10):
    n = 0
    stack = deque([])
    
    for i in range(1, k):
        stack.append((i, i, 1))
    
    wait_list = []
    
    prev = 1
    while stack:
        num, base, l = stack.popleft()
        if l > prev:
            for new_num in wait_list:
                n += 1
                p[k][n] = p[k][n-1] + new_num
                if n == 30: break
            if n == 30: break
            wait_list = []
        
        new_num = getPalBaseNum(num, base // 10, k)
        if is_palindrome(new_num):
            n += 1
            p[k][n] = p[k][n-1] + new_num
            if n == 30: break
        
        new_num = getPalBaseNum(num, base, k)
        if is_palindrome(new_num):
            prev = l
            wait_list.append(new_num)
        
        for i in range(k):
            new_base = base * 10 + i
            new_num = num * k + i
            stack.append((new_num, new_base, l + 1))

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        return p[k][n]