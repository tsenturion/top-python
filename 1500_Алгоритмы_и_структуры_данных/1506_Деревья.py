"""
1506_Деревья
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# бинарное дерево поиска

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
#O(n) - в худшем случае, O(log n) - в среднем случае для сбалансированного дерева

# AVL, красно-черные деревья - самобалансирующиеся деревья для обеспечения O(log n) в худшем случае