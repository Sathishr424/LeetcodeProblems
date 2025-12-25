// Last updated: 12/25/2025, 7:08:15 PM
vector<int> pali;

string intToBinary(int num) {
    if (num == 0)
        return "";
    return intToBinary(num >> 1) + to_string(num % 2);
}

bool isPalindrome(string st) {
    int n = st.length();
    for (int i = 0; i < n / 2; i++) {
        if (st[i] != st[n - i - 1])
            return false;
    }
    return true;
}

struct Init {
    Init() {
        for (int i = 0; i <= 1e6; i++) {
            if (isPalindrome(intToBinary(i))) pali.push_back(i);
        }
    }
} init_instance;


class Solution {
public:
    vector<int> minOperations(vector<int>& nums) {
        vector<int> ret;

        for (int num : nums) {
            int l = 0;
            int r = pali.size() - 1;

            while (l < r) {
                int mid = (l + r) / 2;

                if (abs(pali[mid] - num) <= abs(pali[mid + 1] - num)) {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }

            ret.push_back(abs(pali[l] - num));
        }

        return ret;
    }
};