# Last updated: 12/6/2025, 5:50:59 am
number_dict = {
    0: '',
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
    11: 'Eleven',
    12: 'Twelve',
    13: 'Thirteen',
    14: 'Fourteen',
    15: 'Fifteen',
    16: 'Sixteen',
    17: 'Seventeen',
    18: 'Eighteen',
    19: 'Nineteen',
    20: 'Twenty',
    30: 'Thirty',
    40: 'Forty',
    50: 'Fifty',
    60: 'Sixty',
    70: 'Seventy',
    80: 'Eighty',
    90: 'Ninety',
    100: 'Hundred',
    1000: 'Thousand',
    1000000: 'Million',
    1000000000: 'Billion'
}

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        ret = []
        ten = 1
        def helper(number):
            nonlocal ten
            rem = number % 100
            number //= 100
            if rem <= 20:
                if rem > 0: ret.append(number_dict[rem])
            else:
                r = rem%10
                rem -= r
                if r > 0: ret.append(number_dict[r])
                if rem > 0: ret.append(number_dict[rem])
            rem = number % 10
            number //= 10
            if rem > 0: 
                ret.append('Hundred')
                ret.append(number_dict[rem])
            return number
        
        while num:
            ten *= 100
            if num%1000 > 0 and ten > 100:
                if ten < 1000:
                    ret.append('Hundred')
                elif ten < 1000000:
                    ret.append('Thousand')
                elif ten < 100000000:
                    ret.append('Million')
                else:
                    ret.append('Billion')
            num = helper(num)
        return ' '.join(ret[::-1])