# Leetcode
# 297. Serialize and Deserialize Binary Tree
# https://www.youtube.com/watch?v=u4JAi2JJhI8

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        self.dfs_serializer(root, result)
        # print(result)
        return ",".join(result)
        
    def dfs_serializer(self, root, result):
        if root is None:
            result.append("N")
            return 
        result.append(str(root.val))
        self.dfs_serializer(root.left, result)
        self.dfs_serializer(root.right, result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")
        return self.dfs_deserializer(values)
        
    def dfs_deserializer(self, values):
        # print(values)
        val = values.pop(0)
        if val == "N":
            return None
        node = TreeNode(int(val))
        node.left = self.dfs_deserializer(values)
        node.right = self.dfs_deserializer(values)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
