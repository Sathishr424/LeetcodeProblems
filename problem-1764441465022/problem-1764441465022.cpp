// Last updated: 30/11/2025, 12:07:45 am
1class Solution {
2public:
3    int vowelStrings(vector<string>& words, int left, int right) {
4        int count = 0;
5        unordered_set<char> vowels = {
6            'a', 'e', 'i', 'o', 'u'
7        };
8
9        for (int i=left; i<=right; i++) {
10            string word = words[i];
11            if (vowels.find(word[0]) != vowels.end() && vowels.find(word[word.length() - 1]) != vowels.end()) {
12                count++;
13            }
14        }
15
16        return count;
17    }
18};