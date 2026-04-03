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
        line = "%s" % node.val
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    if node.right is None:
        lines, n, p, x = _display_aux(node.left)
        s = "%s" % node.val
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "_" + s
        second_line = x * " " + "/" + (n - x - 1 + u) * " "
        shifted_lines = [line + u * " " for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

    if node.left is None:
        lines, n, p, x = _display_aux(node.right)
        s = "%s" % node.val
        u = len(s)
        first_line = s + x * "_" + (n - x) * " "
        second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
        shifted_lines = [u * " " + line for line in lines]
        return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

    left, n, p, x = _display_aux(node.left)
    right, m, q, y = _display_aux(node.right)
    s = "%s" % node.val
    u = len(s)

    first_line = (x + 1) * " " + (n - x - 1) * "_" + s + y * "_" + (m - y) * " "
    second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "

    if p < q:
        left += [n * " "] * (q - p)
    elif q < p:
        right += [m * " "] * (p - q)

    zipped_lines = [a + u * " " + b for a, b in zip(left, right)]
    return (
        [first_line, second_line] + zipped_lines,
        n + m + u,
        max(p, q) + 2,
        n + u // 2,
    )


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.result = 0

        def dfs(node, left, length):
            if not node:
                return 0

            self.result = max(self.result, length)

            if left:
                dfs(node.left, False, length + 1)
                dfs(node.right, True, 1)
            else:
                dfs(node.right, True, length + 1)
                dfs(node.left, False, 1)

        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.result


if __name__ == "__main__":
    sol = Solution()
    root = build_tree(
        [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
    )
    print(sol.longestZigZag(root))
