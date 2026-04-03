from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        m = length - n
        if m == 0:
            return head.next

        current = head
        for _ in range(m - 1):
            current = current.next
        current.next = current.next.next

        return head


def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def print_linked_list(node):
    result = []
    while node:
        result.append(str(node.val))
        node = node.next
    print(" -> ".join(result))


if __name__ == "__main__":
    sol = Solution()
    head = create_linked_list([1, 2, 3, 4, 5])
    n = 2
    print_linked_list(sol.removeNthFromEnd(head, n))
