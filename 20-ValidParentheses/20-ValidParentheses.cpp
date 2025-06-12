// Last updated: 12/6/2025, 5:55:10 am
struct Mode{
    int index = -1;
    char type = 'n';
};

class Solution {
public:
    Mode _find(vector<char> &open, vector<char> &close, char c){
        Mode ret;
        for (unsigned int i=0; i<open.size(); i++){
            if (c == open[i]) {ret.index =  i; ret.type = 'o'; return ret;}
            else if (c == close[i]) {ret.index =  i; ret.type = 'c'; return ret;}
        }
        return ret;
    }
    bool isValid(string s) {
        if (s.length() == 0) return 1;
        if (s.length() == 1) return 0;
        vector<char> opened = {'(','{','['};
        vector<char> closed = {')','}',']'};
        vector<int> _stack;
        if (_find(opened, closed, s[0]).type == 'c') return false;
        for (unsigned int i=0; i<s.length(); i++){
            Mode check = _find(opened, closed, s[i]);
            if (check.type == 'c' && _stack.size() <= 0) return false;
            else if (check.type == 'o') _stack.push_back(check.index);
            else if (check.type == 'c' && check.index == _stack[_stack.size()-1])
                _stack.pop_back();
            else return false;
        }
        if (_stack.size() <= 0) return true;
        else return false;
    }
};