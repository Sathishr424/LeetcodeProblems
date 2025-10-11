# Last updated: 11/10/2025, 8:16:54 pm
class ExamTracker:
    def __init__(self):
        self.times = []
        self.scores = []
        self.prefix = [0]

    def record(self, time: int, score: int) -> None:
        self.times.append(time)
        self.scores.append(score)
        self.prefix.append(self.prefix[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        left = bisect_left(self.times, startTime)
        right = bisect_right(self.times, endTime)

        return self.prefix[right] - self.prefix[left]

# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)