# Last updated: 12/6/2025, 5:45:29 am
class StockSpanner:

    def __init__(self):
        self.arr = []

    def next(self, price: int) -> int:
        cnt = 1
        while self.arr and self.arr[-1][0] <= price:
            cnt += self.arr[-1][1]
            self.arr.pop()
        
        self.arr.append((price, cnt))
        return cnt

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)