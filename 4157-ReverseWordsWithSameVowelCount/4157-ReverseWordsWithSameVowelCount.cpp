// Last updated: 12/25/2025, 7:07:52 PM
class Solution {
public:
    string reverseWords(string s) {
        int n = s.size();
        vector<string> words;

        string curr = "";
        for (int i=0; i<n; i++) {
            if (s[i] == ' ') {
                words.push_back(curr);
                curr = "";
                continue;
            }
            curr += s[i];
        }
        words.push_back(curr);
        int v_cnt = 0;
        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
        for (char c: words[0]) {
            if (vowels.find(c) != vowels.end()) v_cnt++;
        }
        
        string res = words[0] + " ";
        for (int i=1; i<words.size(); i++) {
            int cnt = 0;
            for (char c: words[i]) {
                if (vowels.find(c) != vowels.end()) cnt++;
            }
            if (cnt == v_cnt) {
                string rev = "";
                for (int j=words[i].length()-1; j>=0; j--) rev += words[i][j];
                res += rev + " ";
            } else {
                res += words[i] + " ";
            }
        }

        return res.substr(0, res.length() - 1);
    }
};