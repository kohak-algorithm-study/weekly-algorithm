# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # input: 1 -> 2 -> 3 -> 4 -> 5
    # output: 5 -> 4 -> 3 -> 2 -> 1
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = None, head
        # none, 1
        while curr:

            # keypoint: 다음 노드의 포인터를 미리 찍어두고, 현재 노드의 다음을 이전 노드로 설정해준다.
            # 현재 노드의 포인터와 이전 노드에 대한 포인터가 필요하다.

            temp = curr.next  # 현재 노드의 다음 노드를 복사해둠
            curr.next = prev  # 현재 노드의 다음 노드를 이전 노드로 바꿔줌

            prev = curr  # 다음 탐색 노드의 prev를 갱신()
            curr = temp  # 다음 탐색 노드 갱신

        return prev
