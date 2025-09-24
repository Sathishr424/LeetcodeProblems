# Last updated: 24/9/2025, 9:35:54 pm
class LUPrefix:
    def __init__(self, n: int):
        self.n = n
        self.longest_sofar = [False] * (n + 1)
        self.uploaded = [False] * (n + 1)
        self.maxi = 0
        self.uploaded[0] = True
        self.longest_sofar[0] = True

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        self.longest_sofar[video] = self.longest_sofar[video - 1]
        
        if self.longest_sofar[video]:
            self.maxi = max(self.maxi, video)
            index = video + 1
            while index <= self.n and not self.longest_sofar[index] and self.uploaded[index]:
                self.longest_sofar[index] = True
                self.maxi = max(self.maxi, index)
                index += 1

    def longest(self) -> int:
        return self.maxi

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()