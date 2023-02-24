# class Node():
#     def __init__(self, value=None, left=None, right=None, next=None):
#         self.value = value
#         self.left = left
#         self.right = right
#         self.next = next
 
# class Stack():
#     def __init__(self):
#         self.head = None
 
#     def push(self, node):
#         if not self.head:
#             self.head = node
#         else:
#             node.next = self.head
#             self.head = node
 
#     def pop(self):
#         if self.head:
#             popped = self.head
#             self.head = self.head.next
#             return popped
#         else:
#             raise Exception("Stack is empty")
 
# class ExpressionTree():
#     def __init__(self, postfix_exp):
#         self.exp = postfix_exp
#         self.root = None
#         self.createTree(self.exp)

#     def createTree(self, exp):
#         stack = Stack()

#         for c in exp:
#             if c in "+-*/^":
#                 z = Node(c)
#                 x = stack.pop()
#                 y = stack.pop()
#                 z.left = y
#                 z.right = x
#                 stack.push(z)
#             else:
#                 stack.push(Node(c))
#         print("The Inorder Traversal of Expression Tree: ", end="")
#         self.inorder(stack.pop())

#     def inorder(self, x):
#         if not x:
#             return
#         self.inorder(x.left)
#         print(x.value, end=" ")
#         self.inorder(x.right)

class stack:
   def __init__(self):
      self.arr = []
   def push(self, data):
      self.arr.append(data)
   def pop(self):
      try:
         return self.arr.pop(-1)
      except:
         pass
   def top(self):
      try:
         return self.arr[-1]
      except:
         pass
   def size(self):
      return len(self.arr)
# node class for expression tree
class node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
# expression tree class
class exp_tree:
   def __init__(self, postfix_exp):
      self.exp = postfix_exp
      self.root = None
      self.createTree(self.exp)
   def isOperator(self, char):
      optr = [" ", "-", "*", "/", "^"]
      if char in optr: # if given char is operator
         return True # then return true
      return False # else return false
   def createTree(self, exp):
      s = stack()
      # store those operator node whose any child node is NULL
      self.root = node(exp[-1])
      # last character of postfix expression is always an operator
      s.push(self.root)
      # travel on rest of the postfix expression
      for i in "".join(reversed(exp[:-1])):
         curr_node = s.top()
         if not curr_node.right:
            # if right node of current node is NULL
            temp = node(i)
            curr_node.right = temp
            if self.isOperator(i):
               s.push(temp)
         else: # if left node of current node is NULL
            temp = node(i)
            curr_node.left = temp
            # if no child node of current node is NULL
            s.pop() # pop current from stack
            if self.isOperator(i):
               s.push(temp)
   def inorder(self, head):
      # inorder traversal of expression tree
      # inorder traversal = > left, root, right
      if head.left:
         self.inorder(head.left)
      print(head.data, end=" ")
      if head.right:
         self.inorder(head.right)
   def infixExp(self):
      # inorder traversal of expression tree give infix expression
      self.inorder(self.root)
      print()

class Node():
    def __init__(self, left_child_index):
       self.DataValue = ""
       self.LeftChild = left_child_index
       self.RightChild = -1

class ExpressionTree():
    def __init__(self):
       self.Tree = list()
       self.Fringe = list()
       self.root = 0
       self.NextFreeChild = 0
    
    def IsOperator(self, s):
        operator = ["+", "-", "*", "/"]
        if s in operator:
            return True
        return False
    
    def Insert(self, NewToken):
        if self.NextFreeChild == -1:
            return "Tree is Full"

        if self.NextFreeChild == 0:
            self.Tree.append()