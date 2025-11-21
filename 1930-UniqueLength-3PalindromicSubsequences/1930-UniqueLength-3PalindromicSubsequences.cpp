// Last updated: 21/11/2025, 5:16:41 pm
class Solution {
public:
    int countPalindromicSubsequence(string s) {
        int n = s.length();
        int ans = 0;
        int lowercase = 'a';
        for (int a=lowercase; a<lowercase+26; a++) {
            char c = static_cast<char>(a);
            int left = -1;
            int right = -1;
            for (int i=0; i<n; i++) {
                if (s[i] == c) {
                    if(left == -1) left = i;
                    else right = i;
                }
            }
            unordered_set<char> uniq;
            for (int i=left+1; i<right; i++) {
                uniq.insert(s[i]);
            }
            ans += uniq.size();
        }

        return ans;
    }
};