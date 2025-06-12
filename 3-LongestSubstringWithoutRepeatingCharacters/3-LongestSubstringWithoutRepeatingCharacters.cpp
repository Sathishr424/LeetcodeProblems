// Last updated: 12/6/2025, 5:55:51 am
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string list1 = "";
        int lastAdded = -1;
        vector<string> total;
        for (unsigned int i=0; i<s.length(); i++){
            if (s[i] != s[i+1]){
                bool p = true;
                for (unsigned int j=0; j<list1.length(); j++){
                    if (s[i] == list1[j]) p = false;
                }
                if (p){
                    list1.push_back(s[i]);
                    if (lastAdded == -1) lastAdded = i;
                    }
                else{
                    total.push_back(list1);
                    i = lastAdded;
                    lastAdded = -1;
                    list1 = "";
                }
            }else{
                //cout << "else\n";
                bool p = true;
                for (unsigned int j=0; j<list1.length(); j++){
                    if (s[i] == list1[j]) p = false;
                }
                if (p){
                    list1.push_back(s[i]);
                    if (lastAdded == -1) lastAdded = i;
                }
                total.push_back(list1);
                i = lastAdded;
                lastAdded = -1;
                list1 = "";
            }
        }
        total.push_back(list1);
        int maxSize = 0;
        for (unsigned int i=0; i<total.size(); i++){
            //cout << total[i] << endl;
            if (total[i].length() > (unsigned)maxSize) maxSize = total[i].length();
        }
        if (maxSize <= 0 && s.length() > 0) return 1;
        else return maxSize;
    }
};