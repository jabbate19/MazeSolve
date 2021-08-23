class Node:
   def __init__(self, data):
      self.children = None
      self.data = data

   def insert(self, data):
# Compare the new value with the parent node
      if self.data:
         if self.children:
            self.children[self.children.length] = data
         else:
            self.children = [data]
      else:
         self.data = data

# Print the tree
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()