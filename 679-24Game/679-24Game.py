# Last updated: 18/8/2025, 8:03:23 am
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        n = len(cards)
        check = 23.99999
        def rec(index, curr_card, exp, open):
            if index == 3:
                exp += str(curr_card[index])
                if open: exp += ')'
                try:
                    ans = eval(exp)
                    return ans >= check and ans <= 24
                except:
                    return False
            
            for op in ['-', '+', '*', '/']:
                if open and rec(index + 1, curr_card, exp + str(curr_card[index]) + ")" + op, False): return True
                if not open and rec(index + 1, curr_card, exp + str(curr_card[index]) + op + "(", True): return True
                if not open and rec(index + 1, curr_card, exp + "(" + str(curr_card[index]) + op, True): return True
                if rec(index + 1, curr_card, exp + str(curr_card[index]) + op, open): return True
            
            return False

        for i in range(4):
            for j in range(4):
                if j == i: continue
                for k in range(4):
                    if k == i or k == j: continue
                    for l in range(4):
                        if l == i or l == j or l == k: continue
                        # print(cards[i], cards[j], cards[k], cards[l])
                        curr_card = [cards[i], cards[j], cards[k], cards[l]]

                        if rec(0, curr_card, '', False): return True
        
        return False