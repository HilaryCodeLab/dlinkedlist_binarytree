import unittest
from binary_tree import Tree


class Test(unittest.TestCase):

    # Test insert node
    def test_insertion(self):
        sample = Tree(5)
        test = Tree(14)
        self.assertEqual(sample.insert(10),test.insert(10))

    # Test deletion 1
    def test_deletion(self):
        sample = Tree(14)
        sample.insert(2)
        sample.insert(56)
        self.assertNotEqual(sample.delete_node(sample, 56), 0)

    # Test deletion 2
    def test_deletion2(self):
        test = Tree(9)
        test.insert(33)
        test.insert(56)
        self.assertTrue(test.delete_node(test, 9), 0)

    # Type error raise test
    def test_raise_exception(self):
        test = Tree(9)
        test.insert(33)
        test.insert(56)
        self.assertRaises(TypeError, test, "hello")


    
