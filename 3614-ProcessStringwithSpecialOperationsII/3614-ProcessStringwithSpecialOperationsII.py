# Last updated: 14/7/2025, 12:07:14 pm
class Solution:
    def processStr(self, s: str, k: int) -> str:
        total_cnt = 0

        for char in s:
            if char == '*':
                total_cnt = max(0, total_cnt - 1)
            elif char == '#':
                total_cnt += total_cnt
            elif char == '%':
                pass
            else:
                total_cnt += 1
        
        if total_cnt <= k: return '.'
        print(total_cnt)
        for i in range(26):
            a = chr(ord('a') + i)
            # print(a)
            index = k
            cnt = total_cnt
            match = True

            for char in s[::-1]:
                if char == '*':
                    cnt += 1
                elif char == '#':
                    cnt //= 2
                    if index >= cnt:
                        index -= cnt
                elif char == '%':
                    index = cnt - index - 1
                else:
                    if index == cnt - 1 and char == a: break
                    cnt -= 1
                # print(a, index, cnt)
                if index >= cnt:
                    match = False
                    break
            
            if match:
                return a