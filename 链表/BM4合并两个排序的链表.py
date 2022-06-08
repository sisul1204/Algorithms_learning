# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/8 23:07
# @file     : BM4合并两个排序的链表.py
# @software : PyCharm

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        # write code here
        new_head = cur = ListNode(-1)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
                cur = cur.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
                cur = cur.next
        cur.next = pHead1 if pHead1 else pHead2
        return new_head.next




