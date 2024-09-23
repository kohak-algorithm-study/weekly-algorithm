'''
https://leetcode.com/problems/add-two-numbers/
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        result = '['
        head = self
        while head:
            result += f'{head.val}'
            if head.next:
                result += ', '
            head = head.next
        result += ']'
        return result


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        int_l1 = self._convert_integer(l1)
        int_l2 = self._convert_integer(l2)
        return self._convert_to_list_node(int_l1 + int_l2)

    def _convert_integer(self, node: ListNode) -> int:
        result = 0
        i = 0
        while True:
            result += node.val * (10 ** i)
            node = node.next
            i += 1
            if node is None:
                break

        return result

    def _convert_to_list_node(self, n: int) -> ListNode:
        # 맨 뒷자리부터 노드로 만들기
        list_n = list(str(n))

        result = ListNode()
        now = result  # now: while문에서 사용할 포인터 설정
        while list_n:
            now.val = list_n.pop()
            if list_n:  # 남은 숫자가 있을 때만(맨 마지막 숫자는 next를 생성하지 않음)
                now.next = ListNode()
                now = now.next

        return result

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = ListNode()
        now = head

        over_ten = False
        while l1 and l2:
            sum_val = l1.val + l2.val

            if over_ten:
                sum_val = sum_val + 1
                over_ten = False

            if sum_val >= 10:
                sum_val = sum_val % 10
                over_ten = True

            now.val = sum_val
            if l1.next is None and l2.next is None:  # 둘 다 끝일 때
                break

            l1 = l1.next if l1.next else ListNode()
            l2 = l2.next if l2.next else ListNode()

            now.next = ListNode()
            now = now.next

        if over_ten:
            now.next = ListNode(val=1)

        return head


# l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))))))
# l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))
l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))
solution = Solution()
result = solution.addTwoNumbers2(l1, l2)
print(result)
