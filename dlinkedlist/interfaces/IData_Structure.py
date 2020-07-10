import interfaces
from interfaces.data_structures._queue import _queue
from interfaces.data_structures._stack import _stack

"""helps hide list functions, caller won't see list_append or stuff"""
class stack_i():
    def __init__(self):
        self.__set_stack()
    def push(self,data):
        self.__new_stack._push(data)
    def peek(self):
        return self.__new_stack._peek()
    def isEmpty(self):
        return self.__new_stack._isEmpty()
    def pop(self):
        return self.__new_stack._pop()
    def print_list(self):
        self.__new_stack.printlist()
    def __set_stack(self):
        self.__new_stack = self.__get_stack()
    def __get_stack(self):
        return _stack()
    

class queue():
    def __init__(self):
        self.__set_q()
    def enQ(self,data):
        self.__new_queue._enQ(data)
    def deQ(self):
        self.__new_queue._deQ()
    def print_list(self):
        self.__new_queue.printList()
    def __set_q(self):
        self.__new_queue = self.__get_q()
    def __get_q(self):
        return _queue()    