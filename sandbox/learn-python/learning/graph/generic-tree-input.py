from helper import TreeNode

def predefine_generic_tree_inputs():
    # Tree 1
    root1 = TreeNode(1)
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    root1.children.extend([child1, child2])
    
    child1.children.append(TreeNode(4))
    child2.children.append(TreeNode(5))
    
    # Tree 2
    root2 = TreeNode(10)
    child1 = TreeNode(20)
    child2 = TreeNode(30)
    child3 = TreeNode(40)
    root2.children.extend([child1, child2, child3])
    
    child2.children.extend([TreeNode(50),TreeNode(60)])

    # Tree 3
    root3 = TreeNode(100)
    child1 = TreeNode(200)
    root3.children.extend([child1, TreeNode(300)])
    
    child1.children.extend([TreeNode(400),TreeNode(500)])
    
    return root1, root2, root3