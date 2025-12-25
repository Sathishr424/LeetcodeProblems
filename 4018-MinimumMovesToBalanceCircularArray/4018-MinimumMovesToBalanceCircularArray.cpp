// Last updated: 12/25/2025, 7:09:06 PM
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = balance.size();

        long long pos = 0;
        long long neg = 0;
        for (int num: balance) {
            if (num <= 0) pos += num;
            else neg += -num;
        }

        if (neg > pos) return -1;

        vector<int> left;
        deque<int> right;
        for (int i=0; i<n; i++) {
            if (balance[i] > 0) {
                left.push_back(i);
            }
        }

        for (int i=0; i<n; i++) {
            if (balance[i] > 0) {
                right.push_back(i + n);
            }
        }
        
        for (int i=0; i<n; i++) {
            if (balance[i] > 0) {
                right.push_back(i + n * 2);
            }
        }
        
        long long op = 0;

        for (int i=n; i<n+n; i++) {
            int index = i % n;
            while (balance[index] < 0) {
                while (right.front() <= i) {
                    right.pop_front();
                }
                int l_index = i - left.back();
                int r_index = right.front() - i;

                if (l_index < r_index) {
                    int can = min(-balance[index], balance[left.back() % n]);
                    balance[left.back() % n] -= can;
                    balance[index] += can;
                    op += can * 1LL * l_index;
                    if (balance[left.back() % n] == 0) left.pop_back();
                } else {
                    int can = min(-balance[index], balance[right.front() % n]);
                    balance[right.front() % n] -= can;
                    balance[index] += can;
                    op += can * 1LL * r_index;
                    if (balance[right.front() % n] == 0) right.pop_front();
                }
            }
            if (balance[index] > 0) {
                left.push_back(i);
            }
        }

        return op;
    }
};