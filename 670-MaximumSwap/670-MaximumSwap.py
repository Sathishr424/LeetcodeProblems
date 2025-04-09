# Last updated: 9/4/2025, 11:06:28 pm
class Solution:
    def maximumSwap(self, num: int) -> int:
        stack = []

        backup_num = num
        to_replace = -1
        maxi_index = 0

        maxi_index_final = 0

        digits = 1
        maxi = 0
        max_num = 0
        n = 0

        while num:
            rem = num % 10
            num //= 10

            digits *= 10

            if rem > maxi:
                maxi = rem
                maxi_index = n
            
            if maxi != rem:
                max_num = maxi
                to_replace = rem
                maxi_index_final = maxi_index

                # print(to_replace, max_num, maxi_index_final, n)
            
            n += 1
        
        if to_replace == -1: return backup_num
        
        digits //= 10
        
        # print(to_replace, max_num, maxi_index, n)
        n -= 1
        prev = 0
        num = backup_num
        changed = False

        while num:
            rem = num % digits

            dig = (num - rem) // digits

            if not changed and dig == to_replace:
                dig = max_num
                changed = True
            elif maxi_index_final == n:
                dig = to_replace
                prev += dig * digits
                return prev + rem

            prev += dig * digits
            digits //= 10 
            num = rem
            n -= 1
        
        return backup_num