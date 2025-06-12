// Last updated: 12/6/2025, 5:55:17 am
struct St{
    int index;
    string res;
    St(int i, string r){
        index = i;
        res = r;
    }
};

class Solution {
public:
    vector<string> letterCombinations(string digits){
        if (digits.length() <= 0) return {};
        vector<string> ret;
        vector<string> dialPad = {"abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        int n = digits.length();
        
        vector<St> stack = {St(0, "")};
        while (stack.size() > 0){
            St s = stack.back();
            stack.pop_back();
            for (unsigned int i=s.index; i<n; i++){
                for (unsigned int j=0; j<dialPad[(digits[i] - '0') - 2].length(); j++){
                    if (s.res.length()+1 == n) {ret.push_back(s.res + dialPad[(digits[i] - '0') - 2][j]);}
                    else if (s.res.length() + (n-i) >= n) stack.push_back(St(s.index+1, s.res + dialPad[(digits[i] - '0') - 2][j]));
                }
            }
        }return ret;
        
    }
};