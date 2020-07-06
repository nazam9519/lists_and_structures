from modules.linkedlist import linkedlist as S_List

class ISLink_List(object):
     def __init__(self):
         self.list = S_List()
     def insert_after(self,data):
         self.list.insert_after(data)
     def insert_beginning(self,data):
         self.list.insert_beginning(data)
     def print_list(self):
         self.list.printlist()
     def delete_all(self,remdata):
         if self.list.delete(remdata) == True :
            self.print_list()
         else:
             print("issue deleting item")