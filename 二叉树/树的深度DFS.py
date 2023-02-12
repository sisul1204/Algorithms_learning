# * coding:utf-8 *
# Author:sisul
#创建时间：2023/2/12 16:14

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS深度遍历
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    # root.right.right.left = TreeNode(6)
    s = Solution()
    print(s.maxDepth(root))
