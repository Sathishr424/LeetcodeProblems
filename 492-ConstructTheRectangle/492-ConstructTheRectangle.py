# Last updated: 12/6/2025, 5:48:59 am
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        n = int(area ** 0.5)

        for i in range(n, 0, -1):
            if area % i == 0:
                return [area//i, i] 