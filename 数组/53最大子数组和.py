# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/5/29 17:33
# @file     : 53最大子数组和.py
# @software : PyCharm

"""
动态规划
若前一个元素大于0，则加到当前值上
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                res_nums = nums[i-1] + nums[i]
                nums[i] = res_nums
        return max(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2, -1]))
