# This program will be implementing a Linked List class.
# It will also create multiple functions part of the same.
#

class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_node(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)

    def insert_at_beggining(self,data):
        new_head = Node(data,self.head)
        self.head = new_head

    def print_all_nodes(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + " --> " if itr.next else str(itr.data)
            itr = itr.next
        
        print(llstr)
    

ll = LinkedList()
ll.add_node("banana")
ll.add_node("apple")
ll.add_node("grapes")
ll.insert_at_beggining("Fruits")
ll.print_all_nodes()
