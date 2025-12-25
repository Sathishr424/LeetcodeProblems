# Last updated: 12/25/2025, 7:09:15 PM
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        n = len(order)

        ret = []
        for o in order:
            if o in friends:
                ret.append(o)

        return ret