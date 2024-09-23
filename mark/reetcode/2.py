from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_listnode(lst):
    dummy = ListNode()  # 더미 노드 생성
    current = dummy
    for value in lst:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        result_node = head

        over_ten = 0  # 자리올림수를 0으로 초기화

        while l1 or l2 or over_ten:

            sum_val = over_ten  # 이전 자리올림수를 더함

            if l1:
                sum_val += l1.val
                l1 = l1.next

            if l2:
                sum_val += l2.val
                l2 = l2.next

            if sum_val >= 10:
                sum_val = sum_val % 10
                over_ten = 1
            else:
                over_ten = 0

            result_node.next = ListNode(sum_val)
            result_node = result_node.next

        return head.next  # 더미 노드를 제외하고 반환



l1 = list_to_listnode([2,4,3])
l2 = list_to_listnode([5,6,4])
# l1 = list_to_listnode([9,9,9,9,9,9,9])
# l2 = list_to_listnode([9,9,9,9])

Solution().addTwoNumbers(l1, l2)