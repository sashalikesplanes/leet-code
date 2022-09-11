# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
    if head == None:
        return prev
    next_node = head.next
    head.next = prev
    # Do something
    return self.reverseList(next_node, head)
