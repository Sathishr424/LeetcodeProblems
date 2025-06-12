// Last updated: 12/6/2025, 5:55:08 am
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* dummy = new ListNode(0);
        ListNode *node1 = l1, *node2 = l2;
        bool finish1 = 0, finish2 = 0;
        if (node1 == NULL) finish1 = 1;
        if (node2 == NULL) finish2 = 1;
        vector<int> nodes;
        while(true){
            if (finish1 && finish2) break;
            if(!finish1 && node1->next == NULL) {nodes.push_back(node1->val); finish1 = 1;}
            else if(!finish1) {nodes.push_back(node1->val); node1 = node1->next;}
            if (!finish2 && node2->next == NULL) {nodes.push_back(node2->val); finish2 = 1;}
            else if(!finish2){nodes.push_back(node2->val); node2 = node2->next;}
        }sort(nodes.begin(), nodes.end());
        ListNode* ret = dummy;
        for (int item: nodes){
            ret->next = new ListNode(item);
            ret = ret->next;
        }ret = dummy->next;
        delete dummy;
        return ret;
    }
};