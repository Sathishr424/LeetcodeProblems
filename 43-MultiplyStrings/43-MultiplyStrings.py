# Last updated: 12/6/2025, 5:54:35 am
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        arr = []
        
        m = len(num1)
        n = len(num2)
        l = 0
        for i in range(m-1, -1, -1): 
            rem = 0
            curr = []
            for _ in range(m-i-1): curr.append(0)
            for j in range(n-1, -1, -1):
                val = (int(num1[i]) * int(num2[j])) + rem
                rem = val // 10
                curr.append(val % 10)
            if rem: curr.append(rem)
            arr.append(curr)
            l = max(len(curr), l)
        
        rem = 0
        ret = ""
        for i in range(l):
            val = rem
            for a in arr:
                if i < len(a):
                    val += a[i]
            rem = val // 10
            val %= 10
            ret += str(val)
        if rem: ret += str(rem)
        
        return str(int(ret[::-1]))