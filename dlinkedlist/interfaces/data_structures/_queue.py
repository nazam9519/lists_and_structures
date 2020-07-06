from list_pkg import D_list as double_linkedlist

class _queue(double_linkedlist):
    def __init__(self):
        super().__init__()
    def _enQ(self,data):
        self.insert_after(data)
    def _deQ(self):
        self.remove_front()
