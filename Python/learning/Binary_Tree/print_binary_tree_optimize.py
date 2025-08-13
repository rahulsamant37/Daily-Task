from Generic_Binary_Tree_Input import predefine_binary_tree_inputs
from collections import deque

def print_binary_tree_row_wise(root):
    if root is None:
        return
    
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()
        output = f"For {current_node.data}:"
        
        if current_node.left:
            output += f" L-> {current_node.left.data}"
            queue.append(current_node.left)
        else:
            output += " L-> None"
        
        if current_node.right:
            output += f" R-> {current_node.right.data}"
            queue.append(current_node.right)
        else:
            output += " R-> None"
        
        print(output)


# from BinaryTreeNode import BinaryTreeNode
# root1 = BinaryTreeNode(1)
# root1.left = BinaryTreeNode(2)
# root1.right = BinaryTreeNode(3)
# root1.left.left = BinaryTreeNode(4)
# root1.left.right = BinaryTreeNode(6)
# root1.left.left.left = BinaryTreeNode(5)

# print_binary_tree_row_wise(root1)