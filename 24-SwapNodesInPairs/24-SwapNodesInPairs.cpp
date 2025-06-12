// Last updated: 12/6/2025, 5:54:57 am
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
    ListNode* swapPairs(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        ListNode* ret = dummy;
        ListNode* check = head;
        int num = 1, last = 0;
        while (check != NULL){
            if (num == 1) {last = check->val; check = check->next;}
            else if (num == 2){
                ret->next = new ListNode(check->val);
                ret = ret->next;
                ret->next = new ListNode(last);
                ret = ret->next;
                check = check->next;
                num = 0;
            }
            num++;
        }if (num == 2){
           ret->next = new ListNode(last);
        }
        ret = dummy->next;
        delete dummy;
        delete check;
        return ret;
    }
};