# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/8 21:59
# @file     : BM1反转链表.py
# @software : PyCharm

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#

class Solution:
    def ReverseList(self, head: ListNode) -> ListNode:
        # write code here
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
