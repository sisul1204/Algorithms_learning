# * coding:utf-8 *
# Author:sisul
#创建时间：2023/2/12 15:58

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BFS广度遍历
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 保存需要遍历的节点
        lst = []
        # 树的深度
        res = 0
        lst.append(root)
        while len(lst) != 0:
            # 当前层的节点数，即队列的长度
            n = len(lst)
            while n>0:
                node = lst[0]
                if not node.left is None:
                    lst.append(node.left)
                if not node.right is None:
                    lst.append(node.right)
                # 被遍历过的节点出队, 长度减一
                lst.remove(node)
                n -= 1
            res += 1
        return res

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.right.left = TreeNode(6)
    s = Solution()
    print(s.maxDepth(root))

