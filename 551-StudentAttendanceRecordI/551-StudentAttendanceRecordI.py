# Last updated: 12/6/2025, 5:48:28 am
class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)
        absent = 0
        late = 0
        prev = None
        for i in range(len(s)):
            if s[i] == 'A':
                absent += 1
                if absent >= 2: return False
            elif s[i] == 'L':
                if prev == 'L': 
                    late += 1
                    if late == 3: return False
                else:
                    late = 1
            prev = s[i]
        return True
                