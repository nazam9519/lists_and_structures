"""calls stack, queues, lists"""
#driver pgm

from interfaces import queue
from interfaces import stack
from interfaces.data_structures.tree import tree
def main():
    tree1 = tree()
    tree1.insert(5)
    tree1.insert(4)
    tree1.tree_print()
    tree1._tree__treeprint(1)
    return 0
    stacky = stack()
    stacky.print_list()
    stacky.push(1)
    stacky.push(2)
    print(stacky.peek())
    stacky.print_list()
    stacky.pop()
    stacky.print_list()
    stacky.push(3)
    print(stacky.peek())
    stacky.print_list()
    queue1 = queue()
    queue1.enQ(1)
    queue1.enQ(2)
    queue1.print_list()
    return 0
    
if __name__ == "__main__":
	main()

