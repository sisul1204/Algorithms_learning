# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/6/8 23:25
# @file     : BM13判断一个链表是否为回文结构.py
# @software : PyCharm

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类 the head
# @return bool布尔型
#
class Solution:
    def isPail(self , head: ListNode) -> bool:
        # write code here
        list_node = []
        while head:
            list_node.append(head.val)
            head = head.next
        return list_node == list_node[::-1]