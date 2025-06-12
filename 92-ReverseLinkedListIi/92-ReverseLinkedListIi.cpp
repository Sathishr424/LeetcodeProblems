// Last updated: 12/6/2025, 5:53:35 am
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
    void rec(ListNode *node, int index, int &left, int &right, unordered_map<int, int> &hash){
        if (index > right) return;
        hash[left+(right-index)] = node->val;
        rec(node->next, index+1, left, right, hash);
        node->val = hash[index];
    }
    
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        unordered_map<int, int> hash;
        ListNode* node = head;
        for (int i=1; i<left; i++) node = node->next;
        rec(node, left, left, right, hash);
        return head;
    }
};