# Last updated: 22/6/2025, 3:50:32 am
cmax = lambda x, y: x if x > y else y
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        o = []
        z = []
        odd = 0
        even = 0
        for i in range(n):
            nums[i] = nums[i] % 2
            if nums[i] == 0:
                z.append(i)
                even += 1
            else:
                o.append(i)
                odd += 1
    
        if abs(odd - even) > n % 2: return -1

        def process(need):
            o_index = 0
            z_index = 0
            ret = 0
            for i in range(n):
                if need[i] == 1:
                    ret += cmax(0, o[o_index] - i)
                    o_index += 1
                else:
                    ret += cmax(0, z[z_index] - i)
                    z_index += 1
            
            return ret
        
        def doOdd():
            need = [1]
            for i in range(1, n):
                need.append((need[-1] + 1) % 2)
            return process(need)
        
        def doEven():
            need = [0]
            for i in range(1, n):
                need.append((need[-1] + 1) % 2)
            return process(need)
            
        if odd > even:
            return doOdd()
        elif even > odd:
            return doEven()

        return min(doOdd(), doEven())