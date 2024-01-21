class TreeNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return node.height

def is_balanced(root):
    if root is None:
        return True

    balance = height(root.left) - height(root.right)

    # Check if the balance factor is within the allowed range
    if abs(balance) > 1:
        return False

    # Recursively check the balance for the left and right subtrees
    return is_balanced(root.left) and is_balanced(root.right)

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Is the AVL Tree balanced?", is_balanced(root))
