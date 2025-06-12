# Last updated: 12/6/2025, 5:36:54 am
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(num_str, target, start=0, current_sum=0):
            if start == len(num_str):
                return current_sum == target
            for end in range(start, len(num_str)):
                part = int(num_str[start:end+1])
                if canPartition(num_str, target, end+1, current_sum + part):
                    return True
            return False

        total = 0
        for i in range(1, n+1):
            square_str = str(i * i)
            if canPartition(square_str, i):
                total += i * i
        return total
