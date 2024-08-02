class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val):
    # If the root is None, then simply return a new TreeNode with the val
    if not root:
        return TreeNode(val)
    # Using recursion, add new value to the tree, creating a new leaf
    if val == root.val:
        raise Exception("The value {} already exists in the tree".format(val))
    elif val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def get_node_count(root):
    # If the root is None, then return 0
    if not root:
        return 0
    # Using recursion, return the sum of node counts of left subtree and right subtree
    return 1 + get_node_count(root.left) + get_node_count(root.right)

def inorder(root, tree_list):
    # If the root is None, then return empty list
    if not root:
        return []
    # Core part of the inorder traversal
    inorder(root.left, tree_list)
    tree_list.append(root.val)
    inorder(root.right, tree_list)
    # Return the traversed tree in list format
    return tree_list

def print_tree(root):
    # To print the binary search tree from min to max, we use the inorder traversal
    print(inorder(root, []))

def delete_tree(root):
    # Using recursion, loop through all existing node and delete them
    if root:
        delete_tree(root.left)
        delete_tree(root.right)
        root.left = None
        root.right = None
        root = None
    return root
    
def is_in_tree(root, val):
    if not root:
        return False
    if val == root.val:
        return True
    elif val < root.val:
        return is_in_tree(root.left, val)
    else:
        return is_in_tree(root.right, val)

def get_height(root):
    # If root is None, the height is 0
    if not root:
        return 0
    # Use recursion to calculate the heights of left and right subtrees, and return the greatest height
    return 1 + max(get_height(root.left), get_height(root.right))

def get_min(root):
    while root.left:
        root = root.left
    return root.val

def get_max(root):
    while root.right:
        root = root.right
    return root.val

def is_bst(root, min_val = float('-inf'), max_val = float('inf')):
    # If the root is None, then it is a binary search tree so return True
    if not root:
        return True
    # Check if the values are in the correct order in the tree
    if not (min_val < root.val < max_val):
        return False
    # Check also left and right subtrees
    return is_bst(root.left, min_val, root.val) and is_bst(root.right, root.val, max_val)
    
def delete_value(root, val):
    # If the root is None, then raise empty tree error
    if not root:
        raise Exception("The tree is empty.")
    # Delete the node with the target value
    current = root
    # Delete the target value in the left subtree
    if val < current.val:
        if not current.left:
            raise Exception("The value does not exist in the tree.")
        current.left = delete_value(current.left, val)
        return current
    # Delete the target value in the right subtree
    elif val > current.val:
        if not current.right:
            raise Exception("The value does not exist in the tree.")
        current.right = delete_value(current.right, val)
        return current
    # The current node is the node to delete
    else:
        # If the node is a leaf, then delete it
        if not current.left and not current.right:
            return None
        # If the node has only one child, return the child
        if not current.left:
            return current.right
        if not current.right:
            return current.left
        # If the node has two children, find the highest value in the left subtree to replace the node to delete
        parent, node = current, current.left
        while node.right:
            parent, node = node, node.right
        # Check if the node is the only node in the left subtree
        if parent.left is node:
            parent.left = None
        else:
            parent.right = None
        # We simply replace the value to the highest value in the left subtree
        current.val = node.val
        return current

def get_successor(root, val):
    current = root
    successor_val = -1
    while current:
        if val < current.val:
            successor_val = current.val
            current = current.left
        elif val > current.val:
            current = current.right
        else:
            if current.right:
                return get_min(current.right)
            break
    return successor_val


# Initialization for testing
root1 = TreeNode()
print_tree(root1)

# Test for inserting
insert(root1, 4)
insert(root1, -3)
insert(root1, -1)
insert(root1, 7)
print_tree(root1)

# Test for node counting
print(get_node_count(root1))
insert(root1, 1)
print_tree(root1)
print(get_node_count(root1))

# Test for deleting enitre tree
root2 = TreeNode(val = 3)
insert(root2, -10)
insert(root2, 2)
insert(root2, 6)
insert(root2, -2)
print_tree(root2)
root2 = delete_tree(root2)
print_tree(root2)

# Test for checking if a value is in the tree
print_tree(root1)
print(is_in_tree(root1, -1))
print(is_in_tree(root1, 2))

# Test for getting the height of the tree
print(get_height(root1))
print(get_height(root2))
insert(root1, -2)
print(get_height(root1))

# Test for getting the minimum value in the tree
print_tree(root1)
print(get_min(root1))

# Test for getting the maximum value in the tree
print(get_max(root1))

# Test for checking if the tree is a binary search tree
print(is_bst(root1))
root3 = TreeNode(val = 2, left = TreeNode())
root3.left.right = TreeNode(4)
print_tree(root3)
print(is_bst(root3))

# Test for deleting a value in the tree
print_tree(root1)
delete_value(root1, -3)
print_tree(root1)
delete_value(root1, 4)
insert(root1, 2)
print_tree(root1)

# Test for getting the successor of given value
print(get_successor(root1, 0))
print(get_successor(root1, -3))
print(get_successor(root1, 3))