# Last updated: 31/5/2025, 3:16:47 pm
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])
        total = m*n

        arr = []
        cnt = 0
        for i in range(m-1, -1, -1):
            if cnt % 2 == 0:
                for j in range(n):
                    arr.append(board[i][j])
            else:
                for j in range(n-1, -1, -1):
                    arr.append(board[i][j])
            cnt += 1
       
        pos = []

        for i in range(2, min(8, total+1)):
            if arr[i-1] != -1:
                heapq.heappush(pos, (1, arr[i-1]))
            else:
                heapq.heappush(pos, (1, i))
        # print(json.dumps(arr, indent=2))
        ret = float('inf')
        visited = {}
        # print(pos)

        while pos:
            cnt, node = heapq.heappop(pos)
            if node == total:
                # print(node, cnt)
                return cnt
            if cnt >= ret: continue
            if node in visited and visited[node] <= cnt: continue
            visited[node] = cnt
            # print(node, cnt, node+1, min(node+7, total+1))

            for i in range(node+1, min(node+7, total+1)):
                if arr[i-1] != -1:
                    heapq.heappush(pos, (cnt+1, arr[i-1]))
                else:
                    heapq.heappush(pos, (cnt+1, i))
            
            # print(pos)
        
        return ret if ret != float('inf') else -1