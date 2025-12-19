from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def to_int(node):
            num = 0
            multiplier = 1
            while node:
                num += node.val * multiplier
                multiplier *= 10
                node = node.next
            return num

        total = to_int(l1) + to_int(l2)
        if total == 0:
            return ListNode(0)
        
        dummy = ListNode()
        current = dummy

        while total > 0:
            digit = total % 10
            total = total // 10
            current.next = ListNode(digit)
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
    l1_list = [2, 4, 3]
    l2_list = [5, 6, 4]

    l1 = create_linked_list(l1_list)
    l2 = create_linked_list(l2_list)

    print_linked_list(sol.addTwoNumbers(l1, l2))