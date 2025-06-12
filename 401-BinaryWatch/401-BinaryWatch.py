# Last updated: 12/6/2025, 5:49:52 am
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        def add(st):
            mins = 0
            hour = 0
            for i in range(len(st)):
                if st[i] == '1':
                    if i < 4: hour += 2**i
                    else: mins += 2**(i-4)
            if mins < 60 and hour < 12:
                ret.append(f"{hour}:{mins if mins > 9 else f'0{mins}'}")

        def rec(st, cnt):
            if len(st) == 10:
                if cnt == turnedOn: add(st)
                return

            rec(st+'0', cnt)
            if cnt+1 <= turnedOn: rec(st+'1', cnt+1)

        rec("", 0)
        
        return ret
