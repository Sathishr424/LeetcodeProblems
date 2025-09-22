# Last updated: 22/9/2025, 10:31:24 pm
class Solution:
    def largestPalindromic(self, num: str) -> str:
        n = len(num)

        freq = defaultdict(int)

        for dig in num:
            freq[dig] += 1

        max_odd = ''

        nums = []
        for dig in freq:
            if freq[dig] % 2 == 1:
                freq[dig] -= 1
                if max_odd == '' or dig > max_odd:
                    max_odd = dig
            if freq[dig]:
                nums.append(dig)

        nums.sort(reverse=True)
        left = ''
        right = ''

        if len(nums) and nums[0] != '0':
            for dig in nums:
                cnt = freq[dig]
                half = cnt // 2
    
                left += dig * half
                right = dig * half + right

        left += max_odd
        ans = left + right
        if len(ans) == 0: return '0'
        return ans
        
        