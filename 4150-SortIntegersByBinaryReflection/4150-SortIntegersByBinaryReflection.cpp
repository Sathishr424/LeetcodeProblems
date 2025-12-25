// Last updated: 12/25/2025, 7:07:53 PM
struct Vec2 {
    int x;
    int y;
};

class Solution {
public:
    vector<int> sortByReflection(vector<int>& nums) {
        vector<int> ret;
        vector<Vec2> arr;
        
        for (int num: nums) {
            int orig_num = num;
            int rev = 0;
            while (num) {
                rev = rev * 2 + (num & 1);
                num >>= 1;
            }
            arr.push_back({rev, orig_num});
        }

        sort(arr.begin(), arr.end(), [](auto& a, auto& b) {
            return a.x < b.x || (a.x == b.x && a.y < b.y);
        });

        for (auto a: arr) {
            ret.push_back(a.y);
        }

        return ret;
    }
};