# -*- coding:utf-8 -*-
"""
@author:zzh
@file:3_insert_sort.py
@time:2018/3/915:58
"""


def insert_sort(alist):
	"""
	插入排序
		最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
		最坏时间复杂度：O(n2)
		稳定性：稳定
	"""
	n = len(alist)
	# 从第二个位置，即下标为1的元素开始向前插入
	for j in range(1, n):
		for i in range(j, 0, -1):
			# 从第j个元素开始向前比较，如果小于前一个元素，交换位置
			if alist[i] < alist[i - 1]:
				alist[i], alist[i - 1] = alist[i - 1], alist[i]


if __name__ == '__main__':
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	insert_sort(li)
	print(li)
