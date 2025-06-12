// Last updated: 12/6/2025, 5:55:12 am
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *dummy = new ListNode(0);
        ListNode *node = head;
        int cnt = 0;
        while (true){
            if (node->next == NULL) {cnt++; break;}
            cnt++;
            node = node->next;
        }int valid = cnt - n;
        node = head;
        ListNode *ret = dummy;
        for (unsigned int i=0; i<cnt; i++){
            if (i != valid){
                ret->next = new ListNode(node->val);
                ret = ret->next;
                node = node->next;
            }else node = node->next;
        }ret = dummy->next;
        delete dummy, node;
        return ret; 
    }
};