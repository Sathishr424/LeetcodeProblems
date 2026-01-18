# Last updated: 1/18/2026, 7:51:17 PM
1class AuctionSystem:
2    def __init__(self):
3        self.items = defaultdict(list)
4        self.user_bids = defaultdict(dict)
5
6    def addBid(self, userId: int, itemId: int, bidAmount: int) -> None:
7        heapq.heappush(self.items[itemId], (-bidAmount, -userId))
8        self.user_bids[userId][itemId] = bidAmount
9
10    def updateBid(self, userId: int, itemId: int, newAmount: int) -> None:
11        heapq.heappush(self.items[itemId], (-newAmount, -userId))
12        self.user_bids[userId][itemId] = newAmount
13
14    def removeBid(self, userId: int, itemId: int) -> None:
15        self.user_bids[userId][itemId] = -1
16
17    def getHighestBidder(self, itemId: int) -> int:
18        while self.items[itemId] and self.user_bids[ -self.items[itemId][0][1] ][itemId] != -self.items[itemId][0][0]:
19            heapq.heappop(self.items[itemId])
20
21        if self.items[itemId]: return -self.items[itemId][0][1]
22        return -1
23
24# Your AuctionSystem object will be instantiated and called as such:
25# obj = AuctionSystem()
26# obj.addBid(userId,itemId,bidAmount)
27# obj.updateBid(userId,itemId,newAmount)
28# obj.removeBid(userId,itemId)
29# param_4 = obj.getHighestBidder(itemId)