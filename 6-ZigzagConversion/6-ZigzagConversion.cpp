// Last updated: 12/6/2025, 5:55:44 am
class Solution {
public:
    string convert(string s, int numRows){
        if (s.length() <= 0) return "";
        if (s.length() == 1 || s.length() == 2 || numRows == 1) return s;
        string word = "";
        for (int i=0; i<numRows; i++){
            if (i == 0 || i == numRows-1){
                int tmp = i;
                while (true){
                    word.push_back(s[tmp]);
                    tmp+=(numRows+(numRows-2));
                    if (tmp > s.length()-1) break;
                }
            }
            else{
                int sum = 2;
                int ans = i;
                bool first = 1;
                while (true){
                    if (sum % 2 == 0){
                        if (first){
                            word.push_back(s[i]);
                            first = 0;
                        }
                        ans += ((numRows - (i+1))*2);
                    }else{
                        ans += i+1+(i-1);
                    }
                    if (ans > s.length()-1) break;
                    word.push_back(s[ans]);
                    sum++;
                }
            }
        }
        return word;
    }
};