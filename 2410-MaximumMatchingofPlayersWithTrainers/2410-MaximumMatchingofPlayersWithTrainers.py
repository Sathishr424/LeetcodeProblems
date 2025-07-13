# Last updated: 13/7/2025, 11:38:13 am
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        n = len(players)
        m = len(trainers)

        trainers.sort()
        players.sort()

        l = 0
        r = 0
        ret = 0

        while l < n and r < m:
            if players[l] <= trainers[r]:
                ret += 1
                l += 1
                r += 1
            elif players[l] > trainers[r]:
                r += 1
        
        return ret