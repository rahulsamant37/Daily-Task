from helper import TreeNode
from Generic_Tree_input import predefine_generic_tree_inputs

def heightOfTree(root):
    if (root==None):
        return 0
    height = 1
    max_height = 0
    for eachChild in root.children:
        max_height=max(heightOfTree(eachChild),max_height)
    height = height + max_height
    return height

root1, root2, root3 = predefine_generic_tree_inputs()

print(heightOfTree(root1))
print(heightOfTree(root2))
print(heightOfTree(root3))