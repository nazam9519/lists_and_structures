#doubly linked list
from linkedlist import double_linkedlist
from linkedlist import linkedlist
from IData_Structure import stack_i
from IData_Structure import queue

def main():
    
    stacky = stack_i()
    stacky.push(1)
    stacky.push(2)
    print(stacky.peek())
    stacky.pop()
    print(stacky.peek())
    nqueue = queue()
    print("queue time")
    nqueue.enQ(1)
    nqueue.enQ(2)
    nqueue.print_list()
    nqueue.deQ()
    nqueue.print_list()
    nqueue.enQ(3)
    nqueue.print_list()
    return 0
    listitem1 = linkedlist()
    listitem1.delete(1)
    
    x = 10
    i = 1
   # """ while x<=20:
   #     listitem1.insertafter(x)
   #     x+=1
    #listitem1.delete(20)
    #listitem1.printlist() 
    
    listitem2 = double_linkedlist()
    listitem2.delete(1)
    while i<=10:
        listitem2.insertafter(i)
        i+=1
    listitem2.delete(9)
    listitem2.printList()
if __name__ == "__main__":
	main()

