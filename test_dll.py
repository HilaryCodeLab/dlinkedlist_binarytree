import unittest
from double_linked_list import DoublyLinkedList
from double_linked_list import Node

class Test(unittest.TestCase):
    
    def test_insert_at_front(self):
        
    # Method 1:
      dllist = DoublyLinkedList()
      test = DoublyLinkedList()
      self.assertEqual(dllist.insert_at_front(5),test.insert_at_front(5))

    # Method 2:
    # dllist = DoublyLinkedList()
    # self.assertEqual(dllist.insert_at_front(None),None)

    def test_insert_at_end(self):
        dllist = DoublyLinkedList()
        test = DoublyLinkedList()
        self.assertEqual(dllist.insert_at_end(9),test.insert_at_end(9))


    def test_delete_at_front(self):
        dllist = DoublyLinkedList()
        dllist.insert_at_end(6)
        self.assertEqual(dllist.delete_at_front(),None)

    def test_delete_at_end(self):
        dllist = DoublyLinkedList()
        dllist.insert_at_end(10)
        self.assertEqual(dllist.delete_at_end(),None)


    def test_find_node(self):
        dllist = DoublyLinkedList()
        dllist.insert_at_end(10)
        dllist.insert_at_end(4)
        self.assertIsNone(dllist.find_node(5))



    

        



