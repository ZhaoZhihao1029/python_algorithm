# -*- coding:utf-8 -*-
"""
@author:zzh
@file:4_shell_sort.py
@time:2018/3/916:20
"""


def shell_sort(alist):
	"""
	希尔排序
		最优时间复杂度：根据步长序列的不同而不同
		最坏时间复杂度：O(n2)
		稳定性：不稳定
	"""
	n = len(alist)
	gap = n // 2
	while gap > 0:
		# 插入算法
		for j in range(gap, n):
			# j = [gap, gap+1, gap+2, ..., n-1]
			for i in range(j, 0, -gap):
				if alist[i] < alist[i - gap]:
					alist[i], alist[i - gap] = alist[i - gap], alist[i]
		gap //= 2


if __name__ == '__main__':
	li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
	print(li)
	shell_sort(li)
	print(li)
