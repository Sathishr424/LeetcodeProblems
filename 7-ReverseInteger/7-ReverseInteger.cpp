// Last updated: 12/6/2025, 5:55:41 am
class Solution {
public:
    int reverse(int x) {
        if (to_string(x).length() <= 1) return x;
        string ans = to_string(x), ret = "";
        bool neg = 0;
        for (int i=ans.length()-1; i>-1; i--){
            if (ans[i] == '-') neg = 1;
            else ret.push_back(ans[i]);
        }
        try{
            int tmp = stoi(ret);
        }catch (exception &e){
            return 0;
        }
        if (neg) return -(stoi(ret));
        else return stoi(ret);
    }
};