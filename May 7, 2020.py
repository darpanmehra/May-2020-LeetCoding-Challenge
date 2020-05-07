#In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
#Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
#We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
#Return true if and only if the nodes corresponding to the values x and y are cousins.
#Example:
#Input: root = [1,2,3,4], x = 4, y = 3    Output: false
#Input: root = [1,2,3,null,4,null,5], x = 5, y = 4    Output: true

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(node: TreeNode, parent: TreeNode, depth: int):
            if not node or len(output) == 2: return
            else:
                if node.val == x or node.val == y:
                    output.append((parent,depth))
                dfs(node.left, node, depth+1)
                dfs(node.right, node, depth+1)
        output =[]
        dfs(root, None, 0)
        return output[0][0] != output[1][0] and output[0][1] == output[1][1]