# -*- coding:utf-8 -*-
"""
@author:zzh
@file:9_inorder_traversal.py
@time:2019/3/918:19
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def inorder_traversal_recursive(self, root):
        """
        中序遍历（左中右）-递归实现
        :param root:
        :return:
        """
        if not root:
            return []
        return self.inorder_traversal_recursive(root.left) + [root.val] + self.inorder_traversal_recursive(root.right)

    def inorder_traversal_loop(self, root):
        """
        中序遍历（左中右）-循环实现
        :param root:
        :return:
        """
        stack = []
        sol = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                sol.append(curr.val)
                curr = curr.right
        return sol


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    main = Solution()
    main.inorder_traversal_recursive(li)
    main.inorder_traversal_loop(li)
    print(li)
