# class node:
#     def __init__(self, data=None):
#         self.data=data
#         self.next=None
        
# class linked_list:
#     def __init__(self):
#         self.head = node()
        
#     def append_node(self, data):
#         new_node =node(data)
#         current =  self.head
        
#         while current.next != None:
#             current = current.next
            
#         current.next = new_node
        
#     def length(self):
#         current = self.head
#         total = 0
        
#         while current.next !=None:
#             total = 0
#             current = current.next
#             return total
    
#     def display(self):
#         elements = []
#         current_node = self.head
#         while current_node.next != None:
#             current_node = current_node.next
#             elements.append(current_node.data)
#         print (elements)
        
#     def get(self, index):
#         if index >= self.length():
#             print ("Error: 'Get' Index out of range!")
#             return None
#         current_index = 0
#         current_node = self.head
#         while True:
#             current_node = current_node.next
#             if current_index == index:
#                 return current_node.data
#             current_index +=1
        
# my_list = linked_list()
# my_list.display()
# my_list.append_node(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Insertion in linked list
    def insert_at_begining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = new_node
            self.head = new_node
            
# Inserting a Node at a specific position in a linked list
    def insert_at_index(self, data, index):
        if (index==0):
            self.insert_at_begining(data)
            return
        
        position = 0
        current_node = self.head
        while (current_node != None and position +1 != index):
            position = position +1
            current_node = current_node.next
            
        if current_node !=None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print('Index not present')