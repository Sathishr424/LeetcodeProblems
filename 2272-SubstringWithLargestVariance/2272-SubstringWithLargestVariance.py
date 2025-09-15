# Last updated: 15/9/2025, 4:49:46 pm
cmax = lambda x, y: x if x > y else y
cmin = lambda x, y: x if x < y else y
class Solution:
    def largestVariance(self, s: str) -> int:
        # s = [chr(random.randrange(26) + ord('a')) for _ in range(10000)]
        n = len(s)
        s = [ord(char) - ord('a') for char in s]
        max_ans = 0
        there = [0] * 26
        for a in s:
            there[a] = 1

        for i in range(26):
            for j in range(26):
                if i == j or not (there[i] and there[j]): continue

                minor_count = 0
                major_count = 0

                global_max = 0
                local_max = 0
                rem_min_count = 0

                for char in s:
                    if char == j:
                        rem_min_count += 1
                
                for char in s:
                    if char == i:
                        major_count += 1
                    elif char == j:
                        minor_count += 1
                        rem_min_count -= 1
                    
                    local_max = major_count - minor_count
                    if rem_min_count and local_max < 0:
                        local_max = 0
                        major_count = 0
                        minor_count = 0
                    
                    if local_max > global_max and minor_count:
                        global_max = local_max
                
                max_ans = cmax(global_max, max_ans)
                
        return max_ans