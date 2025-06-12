// Last updated: 12/6/2025, 5:51:26 am
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    const rec = (node) => {
        if (!node) return 1;
        else if (!rec(node.next) || node.val != head.val) return 0;
        head = head.next;
        return 1;
    }
    return rec(head);
};