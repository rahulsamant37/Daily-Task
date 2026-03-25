from collections import deque
from BinaryTreeNode import BinaryTreeNode
from print_binary_tree import print_binary_tree

def takeInputBinaryTreeOptimize():
    data = int(input("Enter the data for the Node: "))
    if (data==-1):
        return None
    root = BinaryTreeNode(data)
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()
        
        child_data_left = int(input(f"Enter the data for left child of {current_node.data} : "))
        if (child_data_left!=-1):
            left_child = BinaryTreeNode(child_data_left)
            current_node.left = left_child
            queue.append(left_child)
            
        child_data_right = int(input(f"Enter the data for right child of {current_node.data} : "))
        if (child_data_right!=-1):
            right_child = BinaryTreeNode(child_data_right)
            current_node.right = right_child
            queue.append(right_child)

    return root

# print("Enter the Binary Tree Data (-1 for No Node)")
# root = takeInputBinaryTreeOptimize()
# print_binary_tree(root)
