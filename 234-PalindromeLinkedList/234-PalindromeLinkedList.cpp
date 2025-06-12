// Last updated: 12/6/2025, 5:51:21 am
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* root;
    bool helper(ListNode* node){
        if (!node) return 1;
        else if (!helper(node->next) || node->val != root->val) return 0;
        root = root->next;
        return 1;
    }
    bool isPalindrome(ListNode* head) {
        root = head;
        return helper(head);
    }
};