# -*- coding:utf-8 -*-
"""
@author:zzh
@file:11_levelorder_traversal.py
@time:2019/3/918:38
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelorder_traversal_recursive(self, root):
        """
        层序遍历（从上到下，每层从左至右）-递归实现
        :param root:
        :return:
        """

        def helper(node, level):
            if not node:
                return
            else:
                sol[level - 1].append(node.val)
                if len(sol) == level:  # 遍历到新层时，只有最左边的结点使得等式成立
                    sol.append([])
                helper(node.left, level + 1)
                helper(node.right, level + 1)

        sol = [[]]
        helper(root, 1)
        return sol[:-1]

    def levelorder_traversal_loop(self, root):
        """
        层序遍历（从上到下，每层从左至右）-循环实现
        :param root:
        :return:
        """
        if not root:
            return []
        sol = []
        curr = root
        queue = [curr]
        while queue:
            curr = queue.pop(0)
            sol.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return sol


if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(li)
    main = Solution()
    main.levelorder_traversal_recursive(li)
    main.levelorder_traversal_loop(li)
    print(li)
