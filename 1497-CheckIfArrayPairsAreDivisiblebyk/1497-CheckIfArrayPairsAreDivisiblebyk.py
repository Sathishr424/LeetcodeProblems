# Last updated: 17/7/2025, 7:20:28 pm
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)

        counter_need = [0] * k

        for i in range(n):
            curr = arr[i] % k

            need = (k - curr) % k

            if counter_need[curr]:
                counter_need[curr] -= 1
            else:
                counter_need[need] += 1

        return sum(counter_need) == 0