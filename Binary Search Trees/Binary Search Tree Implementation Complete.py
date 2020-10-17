class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if self.value == value:
            return
        if self.value > value:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = Node(value)
        if self.value < value:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = Node(value)
    
    def find(self, value):
        found = False
        if self.value == value: #check to see if the current node's value matches the search value. NOTE - initiation self == root.
            found = True
        elif self.value == None:
            found = False
        elif self.value < value: #if the value is greater, check the right side of the tree if right side is there.
            if self.right:
                return self.right.find(value)
            else:
                found = False
        else:
            if self.left: #if the value is less, check the left side of the tree if left side is there.
                return self.left.find(value)
            else:
                Found = True
        if found:
            print("Value {} in the tree".format(value))
        else:
            print("value {} not in the tree".format(value))
            
    def pre_order(self):
        if self and self != None:
            print(self.value)
        if self.left:
            self.left.pre_order()
        if self.right:
            self.right.pre_order()
            
    def in_order(self):
        if self:
            if self.left:
                self.left.in_order()
            if self != None:
                print(self.value)
            if self.right:
                self.right.in_order()
            
    def post_order(self):
        if self:
            if self.left:
                self.left.post_order()
            if self.right:
                self.right.post_order()
        if self != None:
            print(self.value)
            
    def delete(self, value, par = None):
        if self.value == value:
            if self.right and self.left:
                parent = self
                successor = self.right
                while successor.left != None:
                    parent = successor
                    successor = successor.left
                    
                self.value = successor.value
                successor.value = None
                if successor.right:
                    parent.left = successor.right
            
            elif self.right and not self.left:
                temp = self.right
                self.value = self.right.value
                self.right = temp.right
                self.left = temp.left
            
            elif not self.right and self.left:
                temp = self.left
                self.value = self.left.value
                self.right = temp.right
                self.left = temp.left
                
            else:
                if self.value > par.value:        #########PROBLEM - Can't seem to find a way to delete leaf nodes  - ########### ---- SOLVED.
                    par.right = None
                else:
                    par.left = None
                    
        elif self.value < value:
            if self.right:
                par = self
                cur = self.right
                return self.right.delete(value, par)
            else:
                return
        else:
            if self.left:
                par = self
                return self.left.delete(value, par)
            else:
                return
            
    def getheight(self):
        if self.left and self.right:
            return 1 + max(self.left.getheight(), self.right.getheight())
        elif self.left and not self.right:
            return 1 + self.left.getheight()
        elif not self.left and self.right:
            return 1 + self.right.getheight()
        else:
            return 1

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            return self.root.insert(value)
        
    def find(self, value):
        if self.root == None:
            print("No tree to find values on")
        else:
            return self.root.find(value)
    
    def pre_order(self):
        print("1....2...3...Pre Order Traversal initiated")
        self.root.pre_order()
    
    def in_order(self):
        print("1....2...3...In Order Traversal initiated")
        self.root.in_order()
    
    def post_order(self):
        print("1....2...3...Post Order Traversal initiated")
        self.root.post_order()
    
    def delete(self, value):
        if self.root:
            return self.root.delete(value)
        else:
            print("no tree to remove value from")
    
    def getheight(self):
        if self.root:
            return self.root.getheight()
        else:
            return -1
            
            
#DRIVER CODE        
t = Tree()
t.insert(50)
t.insert(30)
t.insert(20)
t.insert(40)
t.insert(32)
t.insert(34)
t.insert(36)
t.insert(70)
t.insert(60)
t.insert(65)
t.insert(80)
t.insert(75)
t.insert(85)


t.delete(20)
t.find(85)
t.find(20)
t.find(70)
t.find(40)
#t.find(65)
#t.find(32)
#t.find(34)
#t.find(36)
#print("PRE DELETE")
print(" ")
#t.in_order()
#print(" ")
#t.pre_order()
#print(" ")
t.post_order()
print(" ")
print(t.getheight())
t.delete(36)
print(t.getheight())
t.find(36)
