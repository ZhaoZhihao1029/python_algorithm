# -*- coding:utf-8 -*-
"""
@author:zzh
@file:12_binary_tree.py
@time:2019/3/919:08
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def premid_get_post(self, pre, mid, res):
        """
        已知前序和中序，求后序
        :param pre:
        :param mid:
        :param res:
        :return:
        """
        if len(pre) == 1:
            res.append(pre[0])
            return
        if len(pre) == 0:
            return
        root = pre[0]
        root_index = mid.index(root)
        self.premid_get_post(pre[1:root_index + 1], mid[:root_index], res)
        self.premid_get_post(pre[root_index + 1:], mid[root_index + 1:], res)
        res.append(root)
        return res


if __name__ == '__main__':
    main = Solution()
    # 已知前序和中序，求后序
    # res = main.premid_get_post([1, 2, 4, 5, 8, 9, 11, 3, 6, 7, 10], [4, 2, 8, 5, 11, 9, 1, 6, 3, 10, 7], [])
    res = main.premid_get_post('CABEFDHG', 'BAFECHDG', [])
    # res = [4, 8, 11, 9, 5, 2, 6, 10, 7, 3, 1]
    print(res)