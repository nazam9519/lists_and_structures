from data_structures import priv_stack
from data_structures import _queue

class stack_i():
    def __init__(self):
        self._stack = priv_stack()
    def push(self,data):
        self._stack._push(data)
    def peek(self):
        return self._stack._peek()
    def isEmpty(self):
        return self._stack._isEmpty()
    def pop(self):
        return self._stack._pop()

class queue():
    def __init__(self):
        self.new_queue = _queue()
    def enQ(self,data):
        self.new_queue._enQ(data)
    def deQ(self):
        self.new_queue._deQ()
    def print_list(self):
        self.new_queue.printList()
        