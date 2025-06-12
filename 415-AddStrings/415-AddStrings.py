# Last updated: 12/6/2025, 5:49:38 am
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        
        index = len(num1)-1
        rem = 0
        ret = ""
        
        for i in range(len(num2)-1, -1, -1):
            val = int(num2[i]) + int(num1[index]) + rem
            rem = val // 10
            val %= 10
            ret += str(val)
            index -= 1
        
        for i in range(index, -1, -1):
            val = int(num1[i]) + rem
            rem = val // 10
            val %= 10
            ret += str(val)
    
        if rem: ret += str(rem)

        return ret[::-1]
        

            
