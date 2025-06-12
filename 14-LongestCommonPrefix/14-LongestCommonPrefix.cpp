// Last updated: 12/6/2025, 5:55:23 am
class Solution {
public:
    bool findStr(string x, string c){
        for (unsigned int i=0; i<c.length(); i++){
            if (x[i] != c[i]) return false;
        }return true;
    }
    string longestCommonPrefix(vector<string>& strs){
        if (strs.size() <= 0) return "";
        for (unsigned int i=0; i<strs.size(); i++){
            if (strs[i].length() <= 0) return "";
        }
        if (strs.size() == 1) return strs[0];
        string let = ""; let.push_back(strs[0][0]);
        int index = 1;
        bool match = 1;
        while (match){
            for (unsigned int i=1; i<strs.size(); i++){
                if (!findStr(strs[i], let)) {match = 0; let.pop_back(); break;}
            }if (!match) break;
            if (index < strs[0].length()) let.push_back(strs[0][index]);
            else match = 0;
            index++;
        }return let;
    }
};