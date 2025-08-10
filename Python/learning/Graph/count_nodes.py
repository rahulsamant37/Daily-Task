from helper import TreeNode, print_tree_detailed

def count_nodes(root):
    if(root==None):
        return 0
    numberOfNodes = 1
    
    for eachChild in root.children:
        numberOfNodes+=count_nodes(eachChild)
    
    return numberOfNodes

