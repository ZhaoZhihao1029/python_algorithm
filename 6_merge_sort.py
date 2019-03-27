# -*- coding:utf-8 -*-
"""
@author:zzh
@file:6_merge_sort.py
@time:2018/3/1218:17
"""


def merge_sort(alist):
    """
    归并排序
        最优时间复杂度：O(nlogn)
        最坏时间复杂度：O(nlogn)
        稳定性：稳定
    """
    if len(alist) <= 1:
        return alist
    mid = len(alist) / 2
    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    li2 = merge_sort(li)
    print(li2)
