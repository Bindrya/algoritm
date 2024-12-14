class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
       
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next           
            fast = fast.next.next       
            
            if slow == fast:
                return True
        

        return False

def create_linked_list(values, cycle_pos):
    head = ListNode(values[0])
    current = head
    cycle_node = None
    for i, val in enumerate(values[1:], 1):
        new_node = ListNode(val)
        current.next = new_node
        current = new_node
        if i == cycle_pos:
            cycle_node = new_node
    if cycle_pos != -1:
        current.next = cycle_node  
    return head


s = Solution()

# Жишээ 1
head = create_linked_list([3, 2, 0, -4], 1)
print(s.hasCycle(head)) 

# Жишээ 2
head = create_linked_list([1, 2], 0)
print(s.hasCycle(head))  

# Жишээ 3
head = create_linked_list([1], -1)
print(s.hasCycle(head)) 