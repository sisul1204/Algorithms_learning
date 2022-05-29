# -*- coding=utf-8 -*-
# @Author   : lizp
# @time     : 2022/5/29 13:27
# @file     : 744寻找比目标字母大的最小字母.py
# @software : PyCharm

# 遍历，非二分查找
class Solution:
    def nextGreatestLetter(self, letters, target: str) -> str:
        if target >= letters[len(letters) - 1]:
            return letters[0]
        for letter in letters:
            if letter > target:
                return letter


if __name__ == '__main__':
    s = Solution()
    res = s.nextGreatestLetter(['c', 'f', 'j'], 'd')
    print(res)
