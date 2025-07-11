# Last updated: 11/7/2025, 11:58:13 am
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = len(meetings)
        meetings.sort()

        free_rooms = [0] * n
        used = [0] * n

        meetings_heap = meetings[:]
        heapq.heapify(meetings_heap)

        on_going_meetings_heap = []

        while meetings_heap:
            s, e = heapq.heappop(meetings_heap)
            while on_going_meetings_heap and on_going_meetings_heap[0][0] <= s:
                e_, r = heapq.heappop(on_going_meetings_heap)
                free_rooms[r] = 0

            can = False
            for i in range(n):
                if free_rooms[i] == 0:
                    # print((s, e), 'room:', i)
                    can = True
                    heapq.heappush(on_going_meetings_heap, (e, i))
                    used[i] += 1
                    free_rooms[i] = 1
                    break
            
            if not can:
                e_, r = heapq.heappop(on_going_meetings_heap)
                diff = e_ - s
                # print((s, e), 'room:', r, 'modified:', (s + diff, e + diff))
                heapq.heappush(on_going_meetings_heap, (e + diff, r))
                used[r] += 1
        
        max_room = 0
        for i in range(n):
            if used[i] > used[max_room]:
                max_room = i
        # print(used)
        return max_room
