from helper import TreeNode, print_tree_detailed
from Generic_Tree_input import predefine_generic_tree_inputs


def preorder_traversal(root):
    if (root is None):
        return 
    print(root.data, end=" ")
    for eachChild in root.children:
        preorder_traversal(eachChild)

def postorder_traversal(root):
    if root is None:
        return
    for eachChild in root.children:
        postorder_traversal(eachChild)
    
    print(root.data, end=" ")

root1, root2, root3 = predefine_generic_tree_inputs()

print(preorder_traversal(root1))
print(postorder_traversal(root1))
print_tree_detailed(root1)