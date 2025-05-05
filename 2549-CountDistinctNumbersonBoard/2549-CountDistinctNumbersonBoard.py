# Last updated: 5/5/2025, 11:39:53 pm
class Solution:
    def distinctIntegers(self, n: int) -> int:
        uniq = {}

        uniq[n] = 1

        while True:
            new_uniq = {}
            for num in uniq:
                new_uniq[num] = 1
                for i in range(1, n+1):
                    if num % i == 1:
                        new_uniq[i] = 1
            if len(new_uniq) == len(uniq): break
            uniq = new_uniq
        
        return len(uniq)