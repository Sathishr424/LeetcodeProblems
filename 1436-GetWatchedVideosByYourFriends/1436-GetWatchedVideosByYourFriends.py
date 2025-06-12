# Last updated: 12/6/2025, 5:42:23 am
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        ret = defaultdict(int)
        stack = deque([(id, 0)])
        vis = {id: 1}
        while stack:
            _id, l = stack.popleft()
            if l == level:
                for video in watchedVideos[_id]:
                    ret[video] += 1
            else:
                for i in friends[_id]:
                    if i not in vis and l+1 <= level:
                        vis[i] = 1
                        stack.append((i, l+1))
 
        return sorted(list(ret.keys()), key=lambda x: (ret[x], x))
        