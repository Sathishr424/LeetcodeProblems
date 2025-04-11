# Last updated: 11/4/2025, 11:50:29 pm
class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        if finish < int(s): return 0
        dig = len(s)
        s = int(s)
        d = 10 ** dig

        def getVal(val, add):
            left = val // d * d
            
            if (add == 1 and val - left > s) or (add == -1 and val - left < s):
                left //= d
                left += add
            else:
                left //= d
            # print(val, left)
            l = 0
            tmp = 1
            cnt = 0
            while left:
                rem = left % 10
                left //= 10

                if rem > limit:
                    if add == 1: 
                        left += 1
                        rem = 0
                        l = 0
                        # print(left)
                    else:
                        rem = limit
                        if cnt > 0: l = int(str(limit) * cnt)
                
                l = rem*tmp + l
                tmp *= 10
                cnt += 1
            
            return l

        start = getVal(start, 1)
        finish = getVal(finish, -1)

        print(start, finish)
        if start > finish: return 0

        orig = 1
        to_minus = 0

        while finish:
            rem_f = finish % 10
            rem_s = start % 10
            finish //= 10
            start //= 10
            
            to_minus += (limit - rem_f + rem_s) * orig
            orig *= limit + 1

            # print(orig, to_minus)

        return orig - to_minus
