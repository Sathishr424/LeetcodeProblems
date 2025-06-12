// Last updated: 12/6/2025, 5:55:32 am
/**
 * @param {number} num
 * @return {string}
 */

var intToRoman = function(num) {
    rom = ['I', 'V', 'X', 'L', "C", "D", "M"];
    var get = function(n){
        if (n < 4) return rom[cnt].repeat(n);
        else if (n == 4) return rom[cnt] + rom[cnt+1];
        else if (n == 9) return rom[cnt] + rom[cnt+2];
        else return rom[cnt+1] + (rom[cnt].repeat(n-5));
    }
    ret = ""
    cnt = 0
    while (num > 0){
        rem = num % 10
        num = parseInt(num / 10)
        ret = get(rem) + ret
        cnt += 2
    }return ret 
};