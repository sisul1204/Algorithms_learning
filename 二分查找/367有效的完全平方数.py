# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/5/29 08:54
# @file     : 367有效的完全平方数.py
# @software : PyCharm

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0 or num == 1:
            return True
        left = 0
        right = num
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid + 1
            elif mid ** 2 > num:
                right = mid
        return False


if __name__ == '__main__':
    s = Solution()
    b = s.isPerfectSquare(6)
    print(b)

