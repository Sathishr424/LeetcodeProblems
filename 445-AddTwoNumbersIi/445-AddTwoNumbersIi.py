# Last updated: 12/6/2025, 5:49:22 am
def listNodeToNum(node):
    arr = []
    while node != None:
        arr.append(str(node.val))
        node = node.next
    return ''.join(arr)

def arrToListNode(arr,ind):
    if ind < len(arr): return ListNode(arr[ind],arrToListNode(arr,ind+1))
    return None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return arrToListNode(list(str(int(listNodeToNum(l1)) + int(listNodeToNum(l2)))),0)