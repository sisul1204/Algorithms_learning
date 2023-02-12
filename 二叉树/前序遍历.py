# * coding:utf-8 *
# Author:sisul
#创建时间：2023/2/12 17:29
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# BFS广度遍历
class Solution:
    def qianxBianli(self, root:TreeNode):
        lst = []
