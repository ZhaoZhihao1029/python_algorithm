# -*- coding:utf-8 -*-
"""
@author:zzh
@file:2_select_sort.py
@time:2018/3/915:46
"""


def select_sort(alist):
	"""
	选择排序
		最优时间复杂度：O(n2)
		最坏时间复杂度：O(n2)
		稳定性：不稳定（考虑升序每次选择最大的情况）
	"""
	n = len(alist)
	for j in range(n - 1):
		# 记录最小位置
		min_index = j
		# 从j+1位置到末尾选择出最小数据
		for i in range(j + 1, n):
			if alist[min_index] > alist[i]:
				min_index = i
		alist[j], alist[min_index] = alist[min_index], alist[j]


if __name__ == '__main__':
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	select_sort(li)
	print(li)
