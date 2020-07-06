from nodes import *

class linkedlist:                                  
    def __init__(self):
        self.head = None
    def insert_after(self,node):
        nodedata = SNode(node)
        if self.head == None:
            self.head = nodedata
        else:
            temp = self.head
            while temp.nextitem != None:
                temp = temp.nextitem
            temp.nextitem = nodedata
    def insert_beginning(self,node):
        nodedata = SNode(node)
        if self.head == None:
            self.head = nodedata
        else:
            temp = self.head
            self.head = nodedata
            self.head.nextitem = temp
    def printlist(self):
        itemindex = self.head
        while itemindex != None:
            print(itemindex.data, '->',end='')
            itemindex = itemindex.nextitem
        print('')
    def delete(self,remdata):
        if not self.head: return False
        curr = self.head
        if curr.data == remdata:
            self.head = self.head.nextitem
            curr = None
            return True
        while curr.nextitem != None:
            prev = curr
            curr = curr.nextitem
            if curr.data == remdata:
                prev.nextitem = curr.nextitem
                curr = None
                return True
        return False

class double_linkedlist:                               
    def __init__(self):
        self.head = None
        self.tail = None
    def insert_after(self,node):
        nodedata = DNode(node)
        if not self.head: self.head = self.tail = nodedata
        else:
            self.tail.nextitem = nodedata         #set next item in node to point to the passed data
            temp = self.tail.nextitem             #create temporary pointer
            temp.prev = self.tail                 #set previous pointer to point to last item on the list
            self.tail = temp                      #the new item is now the last item             
    def printList(self):
        itemindex = self.head                      
        while itemindex != None:
            print(itemindex.data, '->',end='')
            itemindex = itemindex.nextitem
        print('')
    def reversePrint(self):
        itemindex = self.tail
        while itemindex != None:
            print(itemindex.data,'->',end='')
            itemindex = itemindex.prev
        print('')

    def delete(self,remdata):
        if not self.head: return False
        if self.__checkNone(remdata): return True
        else:
            curr = self.head
            while curr.nextitem != None:
                 curr = curr.nextitem
                 if curr.data == remdata:
                        curr.prev.nextitem = curr.nextitem
                        curr = None
                        return True
            return False
    def remove_front(self):
            temp = self.head
            self.head = self.head.nextitem
            temp = None
    #utility function        
    def __checkNone(self,remdata):
        if self.head.data == remdata:
            self.head = self.head.nextitem
            self.head.prev = None
            return True
        elif self.tail.data == remdata:
            self.tail = self.tail.prev
            self.tail.nextitem = None
            return True
        else: return False
    