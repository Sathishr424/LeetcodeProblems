# Last updated: 17/7/2025, 4:02:26 pm
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        tot = sum(nums)
        @cache
        def rec(l, r, p1_s, p1_turn):
            if l > r:
                return p1_s >= tot - p1_s
            if p1_turn:
                return rec(l+1, r, p1_s + nums[l], not p1_turn) or rec(l, r-1, p1_s + nums[r], not p1_turn)
            else:
                return rec(l+1, r, p1_s, not p1_turn) and rec(l, r-1, p1_s, not p1_turn)
        
        ans = rec(0, len(nums)-1, 0, True)
        rec.cache_clear()
        return ans