# Last updated: 3/8/2025, 12:30:12 am
class FrequencyTracker:
    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_cnt = defaultdict(int)

    def add(self, number: int) -> None:
        if self.freq[number]:
            self.freq_cnt[self.freq[number]] -= 1
        self.freq[number] += 1
        self.freq_cnt[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number]:
            self.freq_cnt[self.freq[number]] -= 1
            self.freq[number] -= 1
            self.freq_cnt[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_cnt[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)