from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        print(head)
        origin_list = head
        reverse_list = None

        while origin_list:
            next = origin_list.next
            origin_list.next = reverse_list

            reverse_list = origin_list
            origin_list = next

        return reverse_list


head = ListNode(1)
curr_node = head

new_node = ListNode(2)
curr_node.next = new_node
curr_node=curr_node.next

curr_node.next = ListNode(3)
curr_node=curr_node.next

curr_node.next = ListNode(4)
curr_node=curr_node.next

curr_node.next = ListNode(5)
curr_node=curr_node.next
print(Solution().reverseList(head))

