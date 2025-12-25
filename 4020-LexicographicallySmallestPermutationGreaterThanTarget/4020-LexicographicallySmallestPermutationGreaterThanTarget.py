# Last updated: 12/25/2025, 7:09:04 PM
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        arr = sorted(list(s))
        stack = deque([('', 0, arr, False)])

        while stack:
            st, st_index, arr, larger = stack.popleft()
            # print(st, st_index, arr)
            if st_index == n:
                if larger: return st
                continue
            if larger:
                stack.append((st + arr[0], st_index + 1, arr[1:], larger))
                continue
            index = bisect_left(arr, target[st_index])
            if index < len(arr):
                if arr[index] == target[st_index]:
                    stack.append((st + arr[index], st_index + 1, arr[:index] + arr[index+1:], False))
                    index = bisect_right(arr, target[st_index])
                    if index < len(arr):
                        stack.append((st + arr[index], st_index + 1, arr[:index] + arr[index+1:], True))
                elif arr[index] > target[st_index]:
                    stack.append((st + arr[index], st_index + 1, arr[:index] + arr[index+1:], True))

        return ''