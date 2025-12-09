from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def take_level_wise_input():
    data = int(input('Enter  the value of root: '))
    if data == -1 :
        return None
    root = Node(data)
    queue = deque([root])
    while len(queue) != 0 :
       current_node = queue.popleft()
       data = int(input(f'Enter The Data of Left Node of {current_node.data}: '))
       if data != -1:
           current_node.left = Node(data)
           queue.append(current_node.left)
       else:
           current_node.left = None
       data = int(input(f'Enter The Data of Right Node of {current_node.data}: '))
       if data != -1:
           current_node.right = Node(data)
           queue.append(current_node.right)
       else:
           current_node.right = None
    return root

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
    

root = take_level_wise_input()
print_binary_tree(root)
    
    