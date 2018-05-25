# -*- coding:utf-8 -*-
"""
@author:zzh
@file:1_bubble_sort.py
@time:2018/3/915:19
"""


def bubble_sort(alist):
	"""
	冒泡排序
		最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
		最坏时间复杂度：O(n2)
		稳定性：稳定
	"""
	n = len(alist)
	for j in range(n - 1):
		for i in range(0, n - 1 - j):
			if alist[i] > alist[i + 1]:
				alist[i], alist[i + 1] = alist[i + 1], alist[i]


if __name__ == '__main__':
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	bubble_sort(li)
	print(li)
