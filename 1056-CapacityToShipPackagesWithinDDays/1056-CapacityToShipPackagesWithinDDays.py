# Last updated: 12/6/2025, 5:44:24 am
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ret = r

        while l <= r:
            ship_cap = (l+r) // 2

            day = 1
            load = 0
            for w in weights:
                if load+w > ship_cap:
                    day += 1
                    load = 0
                load += w
            
            if day <= days:
                ret = ship_cap
                r = ship_cap-1
            else:
                l = ship_cap+1
        
        return ret

