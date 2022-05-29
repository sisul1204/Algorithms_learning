# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/5/29 08:23
# @file     : 69x的平方根.py
# @software : PyCharm

class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        if x == 0 or x == 1:
            return x
        while left < right:
            mid = (left + right) // 2
            if mid ** 2 == x:
                return mid
            elif mid ** 2 < x:
                left = mid + 1
                if left ** 2 > x:
                    return mid
            elif mid ** 2 > x:
                right = mid
                if (right - 1) ** 2 < x:
                    return mid - 1


if __name__ == '__main__':
    s = Solution()
    x = s.mySqrt(1)
    print(x)
