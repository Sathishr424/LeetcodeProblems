# Last updated: 10/11/2026, 8:40:24 AM
1class BusBooking:
2    def __init__(self, n: int):
3        self.n = n
4        self.rows = [[0] * 4 for _ in range(n)]
5        self.cost = 0
6        self.booked = 0
7
8    def toggle(self, seat: str) -> None:
9        index = ord(seat[0]) - ord('A')
10        row = int(seat[1:]) - 1
11
12        if self.rows[row][index]:
13            self.cost -= self.rows[row][index]
14            self.rows[row][index] = 0
15            self.booked -= 1
16        else:
17            s = 1
18            if (index == 0 and self.rows[row][index + 1]) or (index == 3 and self.rows[row][index - 1]):
19                s += 2
20            self.rows[row][index] = s
21            self.cost += s
22            self.booked += 1
23
24    def getTotalTime(self) -> int:
25        return self.cost
26
27    def getMinTime(self) -> int:
28        return self.booked