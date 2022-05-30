#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
 @Desc: 
 @Time: 2022/5/30 18:49
 @Author: lizp
 @Version: 1.0
 @FileName: 189轮转数组.py
 """


class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # print(nums[-1 * k:] + nums[0:len(nums) - k])
        # return nums[-1 * k:] + nums[0:len(nums) - k]
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1, 2, 3, 4, 5, 6, 7], 3))
