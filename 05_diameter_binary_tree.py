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


def height(root):
    if root == None:
        return 0
    
    leftheight = height(root.left)
    rightheight = height(root.right)
    ans = 1 + max(leftheight,rightheight)
    return ans

def diamter(root):
    if root == None:
        return 0
    leftheight = height(root.left) 
    rightheight = height(root.right)
    leftdiameter = diamter(root.left)
    rightdiameter = diamter(root.right)
    dr = max(leftdiameter,rightdiameter,leftheight+rightheight)
    return dr

root = take_level_wise_input()
ans = diamter(root)
print(ans)