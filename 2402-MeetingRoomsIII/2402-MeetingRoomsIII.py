# Last updated: 11/7/2025, 12:06:15 pm
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free_rooms = SortedList([i for i in range(n)])
        used = [0] * n

        meetings.sort()
        on_going_meetings_heap = []

        def assignRoom(e):
            if len(free_rooms) > 0:
                heapq.heappush(on_going_meetings_heap, (e, free_rooms[0]))
                used[free_rooms[0]] += 1
                free_rooms.discard(free_rooms[0])
                return True
            return False

        for s, e in meetings:
            while on_going_meetings_heap and on_going_meetings_heap[0][0] <= s:
                e_, r = heapq.heappop(on_going_meetings_heap)
                free_rooms.add(r)
            
            if not assignRoom(e):
                e_, r = heapq.heappop(on_going_meetings_heap)
                heapq.heappush(on_going_meetings_heap, (e + (e_ - s), r))
                used[r] += 1
    
        max_room = 0
        for i in range(n):
            if used[i] > used[max_room]:
                max_room = i
        return max_room