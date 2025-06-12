// Last updated: 12/6/2025, 5:55:00 am
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        ListNode* dummy = new ListNode(0);
        ListNode* ret = dummy;
        ListNode* check = head;
        int num = 1;
        vector<int> last;
        while (check != NULL){
            if (num < k) {last.push_back(check->val); check = check->next;}
            else if (num == k){
                last.push_back(check->val);
                for (int i=last.size()-1; i>=0; i--){
                    ret->next = new ListNode(last[i]);
                    ret = ret->next;
                }
                check = check->next;
                num = 0;
                last.clear();
            }
            num++;
        }
       for (unsigned int i=0; i<last.size(); i++){
            ret->next = new ListNode(last[i]);
            ret = ret->next;
        }
        ret = dummy->next;
        delete dummy;
        delete check;
        return ret;
    }
};