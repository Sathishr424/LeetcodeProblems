// Last updated: 12/6/2025, 5:55:33 am
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p.length() == 0) return s.length() == 0;
        bool firstmatch = (s.length() > 0 && (s[0] == p[0] || p[0] == '.'));
        
        if (p.length() >=2 && p[1] == '*'){
            return (isMatch(s, p.substr(2)) || (firstmatch && isMatch(s.substr(1),p)));
        }else{
            return (firstmatch && isMatch(s.substr(1),p.substr(1)));
        }
    }
};