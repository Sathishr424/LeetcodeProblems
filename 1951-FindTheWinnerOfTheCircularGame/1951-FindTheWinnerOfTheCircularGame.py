# Last updated: 12/6/2025, 5:39:48 am
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1, n+1)]
        
        start = -1
        while len(arr) > 1:
            new_arr = []
            index = (start + k) % len(arr)
            for i in range(len(arr)):
                if i != index: new_arr.append(arr[i])
                else: 
                    start = i-1
            arr = new_arr
        return arr[0]


