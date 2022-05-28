# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/5/29 06:42
# @file     : 278第一个错误的版本.py
# @software : PyCharm

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid) == False:
                left = mid +1
                # 正确的版本号向前移动一位，看是否出错
                if isBadVersion(left) == True:
                    return left
            elif isBadVersion(mid) == True:
                right = mid
