# Last updated: 12/6/2025, 5:41:02 am
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr = deque(arr)
        curr = 0
        cnt = 0
        while cnt < k and cnt < n:
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
                arr.append(arr.popleft())
            else:
                arr.append(arr.popleft())
            cnt = cnt + 1 if arr[0] == curr else 1
            curr = arr[0]
        return curr

