# Last updated: 12/25/2025, 7:09:46 PM
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        m = len(landStartTime)
        n = len(waterStartTime)

        ret = inf
        for i in range(m):
            s = landStartTime[i]
            d = landDuration[i]
            time = s + d
            for j in range(n):
                s2 = waterStartTime[j]
                d2 = waterDuration[j]

                if s2 > time:
                    ret = min(ret, time + (s2 - time) + d2)
                else:
                    ret = min(ret, time + d2)
        
        for i in range(n):
            s = waterStartTime[i]
            d = waterDuration[i]
            time = s + d
            for j in range(m):
                s2 = landStartTime[j]
                d2 = landDuration[j]

                if s2 > time:
                    ret = min(ret, time + (s2 - time) + d2)
                else:
                    ret = min(ret, time + d2)
    
        return ret