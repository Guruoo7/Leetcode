class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def cycle(self):
        slw_pointer = self.head
        fst_pointer = self.head
        if self.head is not None:
            while fst_pointer is not None and fst_pointer.next is not None:
                slw_pointer = slw_pointer.next
                fst_pointer = fst_pointer.next.next
                if slw_pointer.data == fst_pointer.data:
                    print("The List is loop")

    def print(self):
        iteration = self.head
        llstr = ""
        while iteration:
            llstr += str(iteration.data) + "-->"
            iteration = iteration.next
        print(llstr)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(4)
    ll.insert_at_beginning(3)
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(1)
    ll.print()
    ll.middle_of_element()