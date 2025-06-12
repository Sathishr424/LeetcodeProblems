// Last updated: 12/6/2025, 5:55:36 am
class Solution {
public:
    int toInt(string x){
        string ret = "";
        ret.push_back(x[0]);
        return stoi(ret);
    }
    int getVal(string x, int i){
        string ret = "";
        ret.push_back(x[i]);
        unsigned int tmp = x.length() - (i+1);
        for (unsigned int j=0; j<tmp; j++) ret.push_back('0');
        return stoi(ret);
    }int getValIf(vector<int> &nums, int x){
        for (unsigned int i=0; i<nums.size(); i++){
            if (nums[i] == x){
                return i;
            }
        }return -1;
    }string assignVal(vector<char> &symb, vector<int> &nums, int x, string ret){
        if (toInt(to_string(x)) == 4 || toInt(to_string(x)) == 9){
            for (unsigned int i=0; i<nums.size(); i++){
                if (nums[i] > x && toInt(to_string(x)) == 4){
                    ret.push_back(symb[i-1]);
                    ret.push_back(symb[i]);break;
                }else if (nums[i] > x && toInt(to_string(x)) == 9){
                    ret.push_back(symb[i-2]);
                    ret.push_back(symb[i]);break;
                }
            }
        }else if (x < 1000){
            unsigned int tmp = toInt(to_string(x));
            bool ones = 1;
            if (toInt(to_string(x)) > 5) tmp = toInt(to_string(x)) - 5;
            for (unsigned int i=0; i<nums.size(); i++){
                if (nums[i] > x){
                    for (unsigned int j=0; j<tmp; j++){
                        if (toInt(to_string(x)) > 5){
                            if (ones){
                                ret.push_back(symb[i-1]); ones = 0;
                            }
                           ret.push_back(symb[i-2]); ones = 0;
                        }
                        else ret.push_back(symb[i-1]);
                    }
                break;}
            }
        }else{
            for (int i=0; i<toInt(to_string(x)); i++)
                ret.push_back(symb[symb.size()-1]);
        }return ret;
    }
    string intToRoman(int num) {
            vector<int> nums = { 1,  5, 10, 50, 100, 500,1000};
        vector<char> symbols = {'I','V','X','L','C', 'D', 'M'};
        string str = to_string(num);
        string ret = "";
        for (unsigned int i=0; i<str.length(); i++){
            unsigned int tmp = getVal(str, i);
            int res = getValIf(nums, tmp);
            if (res != -1) ret.push_back(symbols[res]);
            else ret = assignVal(symbols, nums, tmp, ret);
        }
        return ret;
    }
};