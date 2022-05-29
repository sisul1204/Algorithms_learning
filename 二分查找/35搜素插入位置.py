# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/5/29 07:39
# @file     : 35搜素插入位置.py
# @software : PyCharm

class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)
        if target < nums[0]:
            return 0
        if target > nums[len(nums) -1]:
            return len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                if nums[left] > target:
                    return left
            elif nums[mid] > target:
                right = mid
                if nums[right - 1] < target:
                    return right


if __name__ == '__main__':
    s = Solution()
    index = s.searchInsert([1, 3, 5, 6], -1)
    print(index)
