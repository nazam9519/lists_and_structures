class SNode:
    def __init__(self,data=None):                  #set the node to point to nothing 
        self.data = data                           #initial values
        self.nextitem = None
    def get_data(self):
        return self.data
class DNode:
    def __init__(self,data=None):                  #set the node to point to nothing 
        self.data = data                           #initial values
        self.nextitem = None
        self.prev = None
class TNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None