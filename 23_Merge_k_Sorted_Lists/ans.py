from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        values = []
        for node in lists:
            values.append(node.val)
            node = node.next

        values.sort()

        dummy = ListNode(-1)
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next

        return dummy.next


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
    lists = create_linked_list([[1, 4, 5], [1, 3, 4], [2, 6]])
    print_linked_list(sol.mergeKLists(lists))
