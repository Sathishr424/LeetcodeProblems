# Last updated: 2/1/2026, 1:30:33 PM
1class RideSharingSystem:
2    def __init__(self):
3        self.riders = []
4        self.drivers = []
5        self.riderId = 0
6        self.driverId = 0
7        self.driversDeleted = set()
8        self.ridersDeleted = set()
9        self.driversAdded = set()
10        self.ridersAdded = set()
11
12    def addRider(self, riderId: int) -> None:
13        self.riderId += 1
14        heapq.heappush(self.riders, (self.riderId, riderId))
15        self.ridersAdded.add(riderId)
16
17    def addDriver(self, driverId: int) -> None:
18        self.driverId += 1
19        heapq.heappush(self.drivers, (self.driverId, driverId))
20        self.driversAdded.add(driverId)
21
22    def matchDriverWithRider(self) -> List[int]:
23        while self.drivers and self.drivers[0][1] in self.driversDeleted:
24            heapq.heappop(self.drivers)
25        while self.riders and self.riders[0][1] in self.ridersDeleted:
26            heapq.heappop(self.riders)
27
28        if self.riders and self.drivers:  
29            rider = heapq.heappop(self.riders)
30            driver = heapq.heappop(self.drivers)
31            self.driversDeleted.add(driver[1])
32            self.ridersDeleted.add(rider[1])
33            return [driver[1], rider[1]]
34            
35        return [-1, -1]
36
37    def cancelRider(self, riderId: int) -> None:
38        if riderId in self.ridersAdded: self.ridersDeleted.add(riderId)
39
40# Your RideSharingSystem object will be instantiated and called as such:
41# obj = RideSharingSystem()
42# obj.addRider(riderId)
43# obj.addDriver(driverId)
44# param_3 = obj.matchDriverWithRider()
45# obj.cancelRider(riderId)