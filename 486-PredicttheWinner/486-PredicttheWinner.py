# Last updated: 17/7/2025, 3:24:42 pm
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        @cache
        def rec(l, r, p1_s, p2_s, p1_turn):
            if l > r:
                print(p1_s, p2_s, p1_turn, p1_s >= p2_s)
                return p1_s >= p2_s
            if p1_turn:
                return rec(l+1, r, p1_s + nums[l], p2_s, not p1_turn) or rec(l, r-1, p1_s + nums[r], p2_s, not p1_turn)
            else:
                return rec(l+1, r, p1_s, p2_s + nums[l], not p1_turn) and rec(l, r-1, p1_s, p2_s + nums[r], not p1_turn)
        
        return rec(0, len(nums)-1, 0, 0, True)