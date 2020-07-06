from linkedlist import double_linkedlist
from linkedlist import linkedlist as single_ll

class priv_stack(single_ll):
    """stack data structure built on top of linked list"""
    def __init__(self):
        super().__init__()
    def _push(self,data):
        self.insert_beginning(data)
    def _peek(self):
        if self._isEmpty() is True: return self.head.data
    def _isEmpty(self):
        if self.head.data is None: print("empty list")
        else: return True
    def _pop(self):
        temp = self.head
        self.head = self.head.nextitem
        temp = None


class _queue(double_linkedlist):
    def __init__(self):
        super().__init__()
    def _enQ(self,data):
        self.insert_after(data)
    def _deQ(self):
        self.remove_front()
