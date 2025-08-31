from helper import predefine_binary_tree_inputs

root1, root2, root3 = predefine_binary_tree_inputs()

def preorder_traversal(root):
    if root is None:
        return
    print(root.data, end=" ")
    preorder_traversal(root.left)
    preorder_traversal(root.right)

def postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data, end=" ")

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data, end=" ")
    inorder_traversal(root.right)


# print('---------------#### PRE ORDER TRAVERSAL ####---------------')
# preorder_traversal(root1)
# print('\n---------------#### POST ORDER TRAVERSAL ####---------------')
# postorder_traversal(root1)
# print('\n---------------#### IN ORDER TRAVERSAL ####---------------')
# inorder_traversal(root1)

##
# Tree
#       1
#     /   \
#    2     3
#  /  \   /
# 4    5 6