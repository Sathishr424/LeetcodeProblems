# Last updated: 23/6/2025, 11:36:37 am
def is_palindrome(num):
    st = str(num)
    return st == st[::-1]

def getNewBaseAndNum(num, pal, base):
    while pal:
        rem = pal % 10
        num = num * base + rem
        pal //= 10
    return num

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        stack = deque([])
        ret = 0
        
        for i in range(1, k):
            stack.append((i, i, 1))
        
        wait_list = []
        
        prev = 1
        while stack:
            num, base, l = stack.popleft()
            if l > prev:
                for new_num in wait_list:
                    ret += new_num
                    n -= 1
                    if n == 0: return ret
                wait_list = []
            
            new_num = getNewBaseAndNum(num, base // 10, k)
            if is_palindrome(new_num):
                ret += new_num
                n -= 1
                if n == 0: break
            
            new_num = getNewBaseAndNum(num, base, k)
            if is_palindrome(new_num):
                prev = l
                wait_list.append(new_num)
            
            for i in range(k):
                new_base = base * 10 + i
                new_num = num * k + i
                stack.append((new_num, new_base, l + 1))
        
        return ret