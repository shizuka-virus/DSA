

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)

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

print_binary_tree(root)
