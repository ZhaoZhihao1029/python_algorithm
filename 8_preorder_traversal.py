# -*- coding:utf-8 -*-
"""
@author:zzh
@file:8_preorder_traversal.py
@time:2019/3/918:18
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorder_traversal_recursive(self, root):
        """
        前序遍历（中左右）-递归实现
        :param root:
        :return:
        """
        if not root:
            return []
        return [root.val] + self.preorder_traversal_recursive(root.left) + self.preorder_traversal_recursive(root.right)

    def preorder_traversal_loop(self, root):
        """
        前序遍历（中左右）-循环实现
        :param root:
        :return:
        """
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                sol.append(curr.val)
                stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()
        return sol


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    main = Solution()
    main.preorder_traversal_recursive(li)
    main.preorder_traversal_loop(li)
    print(li)
