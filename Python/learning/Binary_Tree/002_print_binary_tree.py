from helper import predefine_binary_tree_inputs

def print_binary_tree(root):
    if root is None:
        return
    print(root.data, end=" :----------> ")
    if root.left is not None:
        print(f"L-> {root.left.data}", end=", ")
    else:
        print("L-> None", end=", ")
    if root.right is not None:
        print(f"R-> {root.right.data}", end=", \n")
    else:
        print("R-> None", end=", \n")
    print_binary_tree(root.left)
    print_binary_tree(root.right)

root1, root2, root3 = predefine_binary_tree_inputs()

# print_binary_tree(root1)