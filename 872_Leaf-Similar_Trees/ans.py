from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    n = len(values)

    while i < n:
        current = queue.popleft()

        if i < n and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        if i < n and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root

def print_tree(node):
    lines, _, _, _ = _display_aux(node)
    for line in lines:
        print(line)

def _display_aux(node):
    if node.right is None and node.left is None:
        line = '%s' % node.val
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = '%s' % node.val
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
        second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
        shifted_lines = [line + u * ' ' for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = '%s' % node.val
        u = len(s)
        first_line = s + x * '_' + (n - x) * ' '
        second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
        shifted_lines = [u * ' ' + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = '%s' % node.val
    u = len(s)
    
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
    
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
        
    zipped_lines = [a + u * ' ' + b for a, b in zip(left, right)]
    return [first_line, second_line] + zipped_lines, n + m + u, max(p, q) + 2, n + u // 2

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node, out):
            if not node:
                return
            if not node.left and not node.right:
                out.append(node.val)
                return
            dfs(node.left, out)
            dfs(node.right, out)

        r1, r2 = [], []
        dfs(root1, r1)
        dfs(root2, r2)
        
        return r1 == r2

if __name__ == "__main__":
    sol = Solution()
    root1 = build_tree([3,5,1,6,2,9,8,None,None,7,4])
    root2 = build_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    print(sol.leafSimilar(root1, root2))