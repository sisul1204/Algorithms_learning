# * coding:utf-8 *
# Author:sisul
#创建时间：2023/2/12 17:55

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def midBianli(self, root:TreeNode):
        if root is None:
            return None
        lst = []
        # lst.append(root)
        res = []
        while len(lst) != 0 or root is not None:
            while(not root is None):
                lst.append(root)
                # print(lst)
                root = root.left
            root = lst.pop()
            res.append(root)
            root = root.right
        return res


if __name__ == '__main__':
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right = TreeNode('C')
    root.right.right = TreeNode('F')
    s = Solution()
    res = s.midBianli(root)
    for r in res:
        print(r.val)