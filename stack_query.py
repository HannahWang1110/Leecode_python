# PART_1 STACK
# 20. Valid Parentheses(有效的括号)


class Solution:
    def isValid(self, s: str) -> bool:

        dic = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []
        for param in s:
            if param in dic:
                stack.append(param)
            else:
                if stack:
                    last = stack.pop()
                    if dic[last] != param:
                        return False
                else:
                    return False
        return not stack

# 144. Binary Tree Preorder Traversal(二叉树的前序遍历)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        output = []
        while stack:
            node = stack.pop()
            if not node:
                continue
            output.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
        return output

# 150. Evaluate Reverse Polish Notation(逆波兰表达式求值)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = {"+": (lambda x,y: x+y),
               "-": (lambda x,y: x-y),
               "*": (lambda x,y: x*y),
               "/": (lambda x,y: x//y + 1 if x//y<0 and x%y!=0 else x//y)}
                     # x//y if x%y>=0 else x//y + 1)}

        stack = []
        for token in tokens:
            output = 0
            try:
                token = int(token)
                stack.append(token)
            except:
                second = stack.pop()
                first = stack.pop()
                output += ops[token](first, second)
                stack.append(output)
        return stack[0]

# 42. Trapping Rain Water(接雨水)


class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        max_left = [0]
        for h in height:
            max_left.append(max(max_left[-1], h))
        max_right = 0
        for h in height[::-1]:
            max_right = max(max_right,h)
            output += min(max_left.pop(), max_right) - h
        return output

# PART_2 QUERY
# 347. Top K Frequent Elements(前 K 个高频元素)


import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        most = counter.most_common(k)
        return [i[0] for i in most]

# 102. Binary Tree Level Order Traversal(二叉树的层次遍历)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        level = [root]
        output = []
        while level:
            output.append([node.val for node in level])
            LR_pair = [(node.left, node.right) for node in level]
            level = [leaf for LR in LR_pair for leaf in LR if leaf]
        return output

# 279. Perfect Squares


class Solution:
    def numSquares(self, n: int) -> int:

        while n % 4 == 0:
            n = n/4

        if n % 8 == 7:
            return 4

        if int(n**0.5) == n**0.5:
            return 1

        for first in range(1, int(n**0.5)+1):
            if int((n - first**2)**0.5) == (n - first**2)**0.5:
                return 2

        return 3
