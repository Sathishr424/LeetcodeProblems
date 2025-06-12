// Last updated: 12/6/2025, 5:55:27 am
class Solution {
public:
    int checkIf(vector<char> &symb, char c){
        for (int i=0; i<symb.size(); i++){
            if (symb[i] == c) return i;
        }return -1;
    }
    int romanToInt(string s) {
        vector<int> nums = {1,5,10,50,100,500,1000};
        vector<char> symbols = {'I','V','X','L','C','D','M'};
        int ret = 0;
        for (int i=s.length()-1; i>-1; i--){
            int tmp = checkIf(symbols, s[i]);
            if (tmp-1 >= 0 && s[i-1] == symbols[tmp-1]){
                ret += (nums[tmp] - nums[tmp-1]);
                i--;
            }else if (tmp+1 < nums.size() && s[i-1] == symbols[tmp+1]){
                ret += (nums[tmp] + nums[tmp+1]);
                i--;
            }else if (tmp-2 >= 0 && s[i-1] == symbols[tmp-2]){
                ret += (nums[tmp] - nums[tmp-2]);
                i--;
            }else ret += nums[tmp];
        }return ret;
    }
};