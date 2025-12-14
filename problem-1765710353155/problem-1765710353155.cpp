// Last updated: 12/14/2025, 4:35:53 PM
1class Solution {
2public:
3    string reverseWords(string s) {
4        int n = s.size();
5        vector<string> words;
6
7        string curr = "";
8        for (int i=0; i<n; i++) {
9            if (s[i] == ' ') {
10                words.push_back(curr);
11                curr = "";
12                continue;
13            }
14            curr += s[i];
15        }
16        words.push_back(curr);
17        int v_cnt = 0;
18        unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u'};
19        for (char c: words[0]) {
20            if (vowels.find(c) != vowels.end()) v_cnt++;
21        }
22        
23        string res = words[0] + " ";
24        for (int i=1; i<words.size(); i++) {
25            int cnt = 0;
26            for (char c: words[i]) {
27                if (vowels.find(c) != vowels.end()) cnt++;
28            }
29            if (cnt == v_cnt) {
30                string rev = "";
31                for (int j=words[i].length()-1; j>=0; j--) rev += words[i][j];
32                res += rev + " ";
33            } else {
34                res += words[i] + " ";
35            }
36        }
37
38        return res.substr(0, res.length() - 1);
39    }
40};