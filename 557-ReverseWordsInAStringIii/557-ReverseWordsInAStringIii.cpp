// Last updated: 12/6/2025, 5:48:26 am
class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        int prev = 0;
        for (int i=0; i<=n; i++){
            if (s[i] == ' ' || i == n){
                for (int j=0; j<(i-prev)/2; j++){
                    char tmp = s[prev+j];
                    s[prev+j] = s[i-(j+1)];
                    s[i-(j+1)] = tmp;
                }
                prev = i+1;
            }
        }
        return s;
    }
};