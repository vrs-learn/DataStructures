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
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr.next:
            count += 1
            itr = itr.next
        return count

    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            new_node = Node(data,self.head)
            self.head = new_node
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    new_node = Node(data,itr.next)
                    itr.next = new_node
                    break
                itr = itr.next
                count += 1






ll = LinkedList()
ll.add_node("banana")
ll.add_node("apple")
ll.add_node("grapes")
ll.insert_at(2,"LAUKI")
ll.print_all_nodes()
