class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

    def __repr__(self):
        return self.data


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # add new node to the front of list
    def insert_at_front(self,new_data):
        new_node = Node(data=new_data)
       
        # first, check if it is an empty list
        if self.head is None:
            self.head = new_node
            # print("node inserted to new list")
            return
        # set new node as the front node
        new_node.next = self.head
        self.head.previous = new_node
        # as front self.head point to NULL, self head is basically the new_node
        self.head = new_node

    def insert_at_end(self,data):
        # check if the list is empty
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            # print('node inserted to new list')
            return
        
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.previous = last

    def display_list(self, node):
        # display list in forward direction
        node = self.head
        while node is not None:
            print(node.data),
            node = node.next
            return

    def delete_at_front(self):
        # check if it is empty list
        if self.head is None:
            print("list is empty")
            return
        # check if the list only has one element
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next 
        self.head.previous = None

    def delete_at_end(self):
        # check if it is empty list
        if self.head is None:
            print("list is empty")
            return
        # check if the list only has one element
        if self.head.next is None:
            self.head = None
            return
        # else set the next node of last node to last
        last = self.head.next 
        # transverse to the last node
        while last.next is not None:
            last = last.next
        # set next of previous node to None
        last.previous.next = None

    def find_node(self, item):
        is_found = False
        i = 1
        for node in self:
            i = i + 1
            if node.data == item:
                print("element found in position " + str(i))
                is_found = True
                return node
        print("Not found")
        return None

    def __iter__(self):
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next
               
cardValues = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cardSuits = ["Diamond", "Spade", "Heart", "Club"]
for suit in cardSuits:
            for value in cardValues:
                node = Node(suit + " " + value)
                dllist = DoublyLinkedList()
                dllist.insert_at_front(node)
                # dllist.insert_at_end(node)
                # dllist.delete_at_end()
                dllist.display_list(dllist.head)

# dllist = DoublyLinkedList()
# element = Node("Diamond" + " " + "7")

# dllist.insert_at_front("Ace")
# dllist.insert_at_front("2")
# dllist.insert_at_front("3")
# dllist.insert_at_end(4)
# dllist.insert_at_end(5)
# dllist.insert_at_end(6)
# dllist.delete_at_front()
# dllist.delete_at_end()
# dllist.find_node(5)
# dllist.display_list(dllist.head)
