class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev_node = None
        
        if not current_node:
            return None
        
        while True:
            

            # update current node
            # update prev node
            
            next_node = current_node.next
            current_node.next = prev_node
            
            if next_node == None:
                return current_node
            
            prev_node = current_node
            current_node = next_node

        return prev_node
