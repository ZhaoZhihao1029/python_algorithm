# -*- coding:utf-8 -*-
"""
@author:zzh
@file:5_quick_sort.py
@time:2018/3/917:05
"""


def quick_sort(alist, start, end):
    """
    快速排序
        最优时间复杂度：O(nlogn)
        最坏时间复杂度：O(n2)
        稳定性：不稳定
    """
    # !!!递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid_value = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end
    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and mid_value <= alist[high]:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and mid_value > alist[low]:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid_value

    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    quick_sort(li, 0, len(li) - 1)
    print(li)
