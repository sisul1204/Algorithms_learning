#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
 @Desc: 
 @Time: 2022/5/30 18:33
 @Author: lizp
 @Version: 1.0
 @FileName: 977有序数组的平方.py
 """

class Solution:
    def sortedSquares(self, nums):
        square_list = [x ** 2 for x in nums]
        return sorted(square_list)

if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4, -1, 0, 3, 10]))
