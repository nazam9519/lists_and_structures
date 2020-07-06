"""calls stack, queues, lists"""
from interfaces import queue
from interfaces import stack

def main():
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

