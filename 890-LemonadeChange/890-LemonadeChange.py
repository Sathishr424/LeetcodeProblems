# Last updated: 12/6/2025, 5:45:55 am
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for bill in bills:
            if bill > 5:
                c = bill-5
                if c == 5:
                    if not fives: return False
                    fives -= 1
                    tens += 1
                elif c == 15:
                    if tens and fives:
                        tens -= 1
                        fives -= 1
                    elif fives < 3: return False
                    else: fives -= 3
            else: fives += 1
        return True
