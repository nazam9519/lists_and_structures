class SNode:
    def __init__(self,data=None):                  #set the node to point to nothing 
        self.data = data                           #initial values
        self.nextitem = None
class DNode:
    def __init__(self,data=None):                  #set the node to point to nothing 
        self.data = data                           #initial values
        self.nextitem = None
        self.prev = None