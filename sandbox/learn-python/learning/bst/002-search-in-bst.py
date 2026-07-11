# from helper import create_predefined_bsts

def search_in_bst(root, value):
    if root is None:
        return False
    if (root.data == value):
        return True
    elif (value < root.data):
        return search_in_bst(root.left, value)
    else:
        return search_in_bst(root.right, value)

# root1, root2, root3 = create_predefined_bsts()
# print(search_in_bst(root1, 18))
# print(search_in_bst(root1, 13))