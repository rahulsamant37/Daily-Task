from BinaryTreeNode import BinaryTreeNode
# from print_binary_tree import print_binary_tree


def take_input_binarytree():
    data = int(input("Enter the data for the Node: "))
    if (data == -1):
        return None
    node = BinaryTreeNode(data)
    print(f"Enter the left child of {data}")
    node.left = take_input_binarytree()
    print(f"Enter the right child of {data}")
    node.right = take_input_binarytree()
    return node

# print("Enter the Binary Tree Data (-1 for No Node)")
# root = take_input_binarytree()
# print_binary_tree(root)