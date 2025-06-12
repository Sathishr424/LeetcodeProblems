# Last updated: 12/6/2025, 5:46:04 am
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if len(rooms)==1: return True
        keys = rooms[0]
        visited = [False]*len(rooms)
        visited[0] = True
        for i in range(1,len(rooms)):
            if i in keys:
                keys += rooms[i]
                visited[i] = True
        if visited.count(True) == len(rooms): return True
        previous = len(keys)
        while True:
            for i in range(1,len(rooms)):
                if i in keys and not visited[i]:
                    keys += rooms[i]
                    visited[i] = True
            if visited.count(True) == len(rooms): return True
            if len(keys) == previous:
                break
            else: previous = len(keys)
        return visited.count(True) == len(rooms)