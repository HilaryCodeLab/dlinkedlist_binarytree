from card import Card
from double_linked_list import DoublyLinkedList

list = DoublyLinkedList()

valid_rank = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
valid_suit = ['Diamond', "Club", "Heart", "Spade"]

for s in valid_suit:
    for r in valid_rank:
        list.insert_at_end(Card(s,r))
        list.display_list(list.head)
element = Card('Diamond', '8')
list.find_node(element)