# Last updated: 12/6/2025, 5:43:11 am
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # if start == destination: return 0
        if destination < start:
            start, destination = destination, start
        
        arr = [0]
        dis = 0
        for i in range(len(distance)):
            dis += distance[i]
            arr.append(dis)
        s = arr[start]
        d = arr[destination]

        return min(d-s, dis-d+s)

