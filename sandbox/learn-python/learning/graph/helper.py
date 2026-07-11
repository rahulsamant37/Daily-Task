class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    

def print_tree(root):
    if (root==None): ## This is a Edge Case not a base Case
        return
    print(root.data)
    for eachChild in root.children:
        print_tree(eachChild)


def print_tree_detailed(root):
    if (root==None): ## This is a Edge Case not a base Case
        return
    print(root.data,end=": ")
    for eachChild in root.children:
        print(eachChild.data, end=" ")
    print()
    for eachChild in root.children:
        print_tree_detailed(eachChild)


# root = TreeNode(1)


# child1 = TreeNode(2)
# child2 = TreeNode(3)
# child3 = TreeNode(4)

# root.children.extend([child1, child2, child3])
# print(root.data)  # Output: 1
# print(root.children[0].data)  # Output: 2
# print(root.children[1].data)  # Output: 3
# print(root.children[2].data)  # Output: 4

# print_tree(root)

# root2 = TreeNode(1)


# child1 = TreeNode(2)
# child2 = TreeNode(3)
# child3 = TreeNode(4)

# root2.children.extend([child1, child3])
# child1.children.append(child2)
# print_tree_detailed(root)
# print_tree_detailed(root2)

