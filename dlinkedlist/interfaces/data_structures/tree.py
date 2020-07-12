from list_pkg.nodes import TNode
class tree():
    def __init__(self):
        self.count = 1
        self.node = None
    def insert(self,treedata):
        self.node = self.__insert(treedata,self.node)
    def __insert(self,treedata,node):
        if node == None:
            node = TNode()
            node.data = treedata
            self.count = 1
        elif node.data == treedata:
            self.count+=1
        elif node.data > treedata:
            node.left = self.__insert(treedata,node.left)
        elif node.data < treedata:
            node.right = self.__insert(treedata,node.right)
        return node
    def tree_print(self):
        self.__treeprint(self.node)
    def __treeprint(self,node):
        if(node != None):
            self.__treeprint(node.left)
            print(node.data)
            self.__treeprint(node.right)

            
        


