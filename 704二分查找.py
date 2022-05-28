# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/5/29 05:30
# @file     : 704二分查找.py
# @software : PyCharm

"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums)
        # 左闭右开
        while left < right:
            mid = (left + right) //2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid
            elif target == nums[mid]:
                return mid
        return -1


if __name__ == '__main__':
    s = Solution()
    index = s.search([2, 5], 5)
    print(index)
