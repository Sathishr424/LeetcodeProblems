# Last updated: 26/9/2025, 12:18:00 am
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        nums.sort()
        target.sort()

        even = []
        odd = []
        for num in nums:
            if num % 2:
                odd.append(num)
            else:
                even.append(num)
        
        t_even = []
        t_odd = []
        for num in target:
            if num % 2:
                t_odd.append(num)
            else:
                t_even.append(num)
        
        def solve(x, y):
            op = 0
            for i in range(len(x)):
                a = x[i]
                b = y[i]

                if a > b:
                    need = (a - b) // 2
                    op += need
                elif b > a:
                    need = (b - a) // 2
                    op += need
            
            return op
        
        return (solve(even, t_even) + solve(odd, t_odd)) // 2