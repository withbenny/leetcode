from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        odd, even = ListNode(0), ListNode(0)
        odd_curr, even_curr = odd, even
        counter = 1

        while head:
            if counter % 2 == 0:
                even_curr.next = head
                even_curr = even_curr.next
            else:
                odd_curr.next = head
                odd_curr = odd_curr.next

            head = head.next
            counter += 1

        even_curr.next = None
        odd_curr.next = even.next

        return odd.next


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
    head = create_linked_list([2, 1, 3, 5, 6, 4, 7])
    print_linked_list(sol.oddEvenList(head))
