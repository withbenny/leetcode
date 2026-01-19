from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        result = []
        n = len(values)
        for i in range(n // 2):
            result.append(values[i] + values[n - i - 1])

        return max(result)

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