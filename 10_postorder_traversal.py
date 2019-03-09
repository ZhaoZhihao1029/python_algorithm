# -*- coding:utf-8 -*-
"""
@author:zzh
@file:10_postorder_traversal.py
@time:2019/3/918:20
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def postorder_traversal_recursive(self, root):
        """
        后序遍历（左右中）-递归实现
        :param root:
        :return:
        """
        if not root:
            return []
        return self.postorder_traversal_loop(root.left) + self.postorder_traversal_loop(root.right) + [root.val]

    def postorder_traversal_loop(self, root):
        """
        后序遍历（左右中）-循环实现
        :param root:
        :return:
        """
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                sol.append(curr.val)
                stack.append(curr.left)
                curr = curr.right
            else:
                curr = stack.pop()
        return sol[::-1]


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    main = Solution()
    main.postorder_traversal_recursive(li)
    main.postorder_traversal_loop(li)
    print(li)
