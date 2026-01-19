from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        current, prev = None, None
        while slow:
            current = slow.next
            slow.next = prev
            prev = slow
            slow = current

        result = 0
        while prev:
            result = max(result, head.val + prev.val)
            head = head.next
            prev = prev.next

        return result

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
    head = create_linked_list([4,2,2,3])
    print(sol.pairSum(head))