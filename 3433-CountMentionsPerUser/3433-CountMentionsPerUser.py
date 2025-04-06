# Last updated: 6/4/2025, 5:36:37 am
class Solution:
    def countMentions(self, users: int, events: List[List[str]]) -> List[int]:
        n = users
        res = [0] * n

        new_events = []
        for event in events:
            if event[0] == 'MESSAGE':
                new_events.append([1, int(event[1]), event[2]])
            else:
                new_events.append([0, int(event[1]), event[2]])

        new_events.sort(key=lambda x: (x[1], x[0]))

        online_users = [True] * n
        offline = []
        offline_hash = defaultdict(int)

        for event, timestamp, id in new_events:
            if event == 1:
                if id == 'HERE':
                    # print(offline, timestamp, id)
                    while offline and offline[0][0] <= timestamp:
                        t, id = heapq.heappop(offline)

                        if t >= offline_hash[id]:
                            online_users[id] = True
                            offline_hash[id] = 0
                        
                    for i in range(n):
                        res[i] += online_users[i]
                elif id == 'ALL':
                    for i in range(n):
                        res[i] += 1
                else:
                    for u in id.split(' '):
                        res[int(u[2:])] += 1
            else:
                id = int(id)
                heapq.heappush(offline, (timestamp+60, id))
                online_users[id] = False
                offline_hash[id] = max(offline_hash[id], timestamp+60)

        return res
                