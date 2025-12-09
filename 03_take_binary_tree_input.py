class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def take_binary_tree_input():
    data = int(input('Enter The Data For Node',))
    if data == -1 :
        return None
    node = Node(data)
    print(f'For Left of {data}')
    node.left = take_binary_tree_input()
    print(f'For Right of {data}')
    node.right = take_binary_tree_input()
    return node

def print_binary_tree(root):
    if root is None :
        return
    print(root.data,end=' :')
    if root.left is not None:
        print('L->',root.left.data,end=' ')
    else :
        print('L-> None',end=" ")
    if root.right is not None:
        print('R->',root.right.data)
    else :
        print('R-> None')
    print_binary_tree(root.left)
    print_binary_tree(root.right)

root = take_binary_tree_input()
print_binary_tree(root)