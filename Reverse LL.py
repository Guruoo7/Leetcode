class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def print(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            iteration = self.head
            llstr = ''
            while iteration:
                llstr += str(iteration.data) + "-->"
                iteration = iteration.next
            print(llstr)

if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(6)
    ll.insert_at_beginning(7)
    ll.reverse()
    ll.print()