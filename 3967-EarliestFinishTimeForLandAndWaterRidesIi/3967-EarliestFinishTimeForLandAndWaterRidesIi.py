# Last updated: 12/25/2025, 7:09:42 PM
class Solution:
    def earliestFinishTime(self, landStart: List[int], landD: List[int], waterStart: List[int], waterD: List[int]) -> int:
        m = len(landStart)
        n = len(waterStart)
        ret = inf

        land = []
        water = []

        for i in range(m):
            land.append((landStart[i], landD[i]))
        land.sort()
        
        for i in range(n):
            water.append((waterStart[i], waterD[i]))
        water.sort()
        
        waterSmallest = [0] * n
        waterSmallest[0] = water[0][1]
        waterFinished = []
        waterFinished.append(water[0][0] + water[0][1])
        for i in range(1, n):
            waterSmallest[i] = min(waterSmallest[i-1], water[i][1])
            waterFinished.append(water[i][0] + water[i][1])
        waterFinished.sort()
        
        landSmallest = [0] * m
        landSmallest[0] = land[0][1]
        landFinished = []
        landFinished.append(land[0][0] + land[0][1])
        for i in range(1, m):
            landSmallest[i] = min(landSmallest[i-1], land[i][1])
            landFinished.append(land[i][0] + land[i][1])
        landFinished.sort()
    
        # print(landFinished)
        # print(waterFinished)
        # print()
        
        for i in range(m):
            s = land[i][0]
            d = land[i][1]

            time = s + d
            index = bisect_left(water, (time + 1, 0))
            # print((s, d), time, index, 'land')
            if index > 0:
                # print(time + waterSmallest[index - 1])
                ret = min(ret, time + waterSmallest[index - 1])

            index = bisect_left(waterFinished, s)
            if index > 0:
                ret = min(ret, time)
        for i in range(n):
            s = water[i][0]
            d = water[i][1]

            time = s + d
            index = bisect_left(land, (time + 1, 0))
            # print((s, d), time, index, 'water')
            if index > 0:
                # print(time + landSmallest[index - 1])
                ret = min(ret, time + landSmallest[index - 1])
            
            index = bisect_left(landFinished, s)
            if index > 0:
                ret = min(ret, time)

        return ret
