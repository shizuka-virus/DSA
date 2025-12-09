from collections import deque

class Node:
    def __init__(self,data):
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


def diameter(root):
    if root == None :
        return 0,0
    
    left_height,left_diameter = diameter(root.left)
    right_height,right_diameter = diameter(root.right)
    
    root_diamter = left_height+right_height
    current_height = 1 + max(left_height,right_height)
    
    ans = max(root_diamter,left_diameter,right_diameter)
    return current_height,ans

root = take_level_wise_input()
print(diameter(root))
    