# Last updated: 12/6/2025, 5:41:03 am
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("-100"))

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ret = 0
        n = len(arr)

        for i in range(n-2):
            m = SortedList()
            if abs(arr[i] - arr[i+1]) <= a:
                m.add(arr[i+1])
            for j in range(i+2, n):
                if abs(arr[i] - arr[j]) <= c:
                    left = bisect_left(m, arr[j] - b)
                    right = bisect_right(m, b + arr[j])
                    ret += right-left
                if abs(arr[i] - arr[j]) <= a:
                    m.add(arr[j])
        
        return ret