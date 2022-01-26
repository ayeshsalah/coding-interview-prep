# Leetcode
# 449. Serialize and Deserialize BST
# Preorder Traversal using DFS
# https://www.youtube.com/watch?v=u4JAi2JJhI8

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string.
        """
        result = []
        self.serializer(root, result)
        print(",".join(result))
        return ",".join(result)
        
    def serializer(self, node, result):
        if node is None:
            result.append("N")
            return 
        result.append(str(node.val))
        self.serializer(node.left, result)
        self.serializer(node.right, result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree.
        """
        values = data.split(",")
        return self.deserializer(values)
        
    def deserializer(self, values):
        # print(values)
        val = values.pop(0)
        if val == "N":
            return None
        node = TreeNode(int(val))
        node.left = self.deserializer(values)
        node.right = self.deserializer(values)
        return node
    
# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans