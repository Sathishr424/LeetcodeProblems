# Last updated: 11/7/2025, 11:58:42 am
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        m = len(meetings)
        meetings.sort()

        free_rooms = [0] * n
        used = [0] * n

        meetings_heap = meetings[:]
        heapq.heapify(meetings_heap)

        on_going_meetings_heap = []
        max_used_room = 0

        def assignRoom(e):
            nonlocal max_used_room
            for i in range(n):
                if free_rooms[i] == 0:
                    heapq.heappush(on_going_meetings_heap, (e, i))
                    used[i] += 1
                    free_rooms[i] = 1
                    return True
            return False

        while meetings_heap:
            s, e = heapq.heappop(meetings_heap)
            while on_going_meetings_heap and on_going_meetings_heap[0][0] <= s:
                e_, r = heapq.heappop(on_going_meetings_heap)
                free_rooms[r] = 0
            
            if not assignRoom(e):
                e_, r = heapq.heappop(on_going_meetings_heap)
                heapq.heappush(on_going_meetings_heap, (e + (e_ - s), r))
                used[r] += 1
    
        max_room = 0
        for i in range(n):
            if used[i] > used[max_room]:
                max_room = i
        return max_room