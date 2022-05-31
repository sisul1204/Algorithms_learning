# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/5/31 22:07
# @file     : 852山脉数组的峰顶索引.py
# @software : PyCharm

class Solution:
    def peakIndexInMountainArray(self, arr):
        num_max = max(arr)
        for i in range(len(arr)):
            if arr[i] == num_max:
                return i


if __name__ == '__main__':
    s = Solution()
    print(s.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
