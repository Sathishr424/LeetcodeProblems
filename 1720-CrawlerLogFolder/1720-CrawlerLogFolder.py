# Last updated: 12/6/2025, 5:40:49 am
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ret = 0

        for log in logs:
            if log == '../': ret = max(0, ret-1)
            elif log == './': pass
            else: ret += 1
        
        return ret