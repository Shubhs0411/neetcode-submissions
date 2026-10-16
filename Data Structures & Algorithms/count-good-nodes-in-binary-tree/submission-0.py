# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res=0

        stack=[(root, root.val)]
        while stack:
            node, curr_max=stack.pop()

            if node.val>=curr_max:
                res+=1
            new_max=max(node.val, curr_max)
            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))
        return res
        