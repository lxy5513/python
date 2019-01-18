#!coding utf-8
# Definition for a binary tree node.
class Tree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = Tree(0)
root.left = Tree(1)
root.right = Tree(2)

root.right.right = Tree(7)
root.right.left = Tree(8)
import copy
# class Solution:
#     def levelOrderBottom(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         res = []
#         dic = {}
#         if not root:
#             return -1
#         res.append(root.val)
#         dic[root] = 0
#         level_num = 0
#         while dic != {}:
#             level_num += 1
#
#             for i in [k for k, v in dic.items()]:
#                 if i.left :
#                     dic[i.left] = level_num
#                 if i.right:
#                     dic[i.right] = level_num
#
#             print('---',dic.values())
#             for i in [(k,v) for k,v in dic.items()]:
#                 k = i[0]
#                 v = i[1]
#                 if v == level_num-1:
#                     # 在遍历过程中不能对其删除
#                     print(k)
#                     del dic[k]
#             item = []
#             for k in dic.keys():
#                 print(k.val)
#                 item.append(k.val)
#             if item:
#                 res.append(item)
#         print(res)
#         res.reverse()
#         return res

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:return []
        lst = []
        line = [root]
        while any(line):
            import pdb; pdb.set_trace()
            lst.append([node.val for node in line])
            line = [child for node in line for child in (node.left,node.right) if child]

        return lst[::-1]


S = Solution()

S.levelOrderBottom(root)
