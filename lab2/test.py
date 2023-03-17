import unittest
import linked_list

class TestLinkedList(unittest.TestCase):

    def test_append(self):
        #arrange
        ls = linked_list.LinkedList()
        value = "1"

        #act
        ls.append(value)

        #assert
        self.assertEqual(ls.get(0), value)

    def test_insert(self):
        #arrange
        ls = linked_list.LinkedList()

        #act
        ls.append('4')
        ls.insert(0, '0')
        ls.print()

        #arrange
        self.assertEqual(ls.get(1), '4')

        with self.assertRaises(IndexError):
            ls.insert(ls.get_length(), 'Invalid Value')

    def test_length(self):
        #arrange
        ls = linked_list.LinkedList()

        ls.append('1')
        ls.append('2')
        ls.append('3')

        #act
        length = ls.get_length()

        #assert
        self.assertEqual(length, 3)

    def test_get(self):
        #arrange
        ls = linked_list.LinkedList()

        ls.append('1')
        ls.append('2')
        ls.append('3')
        
        #act
        value = ls.get(0)
        #assert
        self.assertEqual(value, '1')

        with self.assertRaises(IndexError):
            ls.get(ls.get_length() + 1)

    def test_clear(self):
        #arrange
        ls = linked_list.LinkedList()
        
        ls.append('1')
        ls.append('2')
        ls.append('3')
        
        #act
        ls.clear()

        #assert
        self.assertEqual(ls.get_length(), 0)

    def test_delete(self):
        #arrange
        ls = linked_list.LinkedList()
        
        ls.append('1')
        ls.append('2')
        ls.append('3')

        #act
        deleted = ls.delete(0)

        #assert
        self.assertEqual(ls.get_length(), 2)
        self.assertEqual(deleted, '1')

        with self.assertRaises(IndexError):
            ls.delete(ls.get_length() + 1)

    def test_delete_all(self):
        #arrange
        ls = linked_list.LinkedList()
        
        ls.append('1')
        ls.append('3')
        ls.append('3')

        #act
        ls.delete_all('3')

        #assert
        self.assertEqual(ls.get_length(), 1)

    def test_find_first(self):
        #arrange
        ls = linked_list.LinkedList()
        
        ls.append('3')
        ls.append('1')
        ls.append('3')

        #act
        first = ls.find_first('3')

        #assert
        self.assertEqual(first, 0)

    def test_find_last(self):
        #arrange
        ls = linked_list.LinkedList()
        
        ls.append('3')
        ls.append('1')
        ls.append('3')

        #act
        last = ls.find_last('3')

        #assert
        self.assertEqual(last, 2)

    def test_reverse(self):
        #arrange
        ls = linked_list.LinkedList()

        ls.append('1')
        ls.append('2')
        ls.append('3')

        #act
        ls.reverse()

        #assert
        self.assertEqual(ls.get(0), '3')

    def test_clone(self):
        #arrange
        ls = linked_list.LinkedList()

        ls.append('1')
        ls.append('2')
        ls.append('3')

        #act
        clone = ls.clone()

        #assert
        self.assertEqual(ls.get(0), clone.get(0))

    def test_extend(self):
        #arrange
        ls1 = linked_list.LinkedList()
        ls2 = linked_list.LinkedList()

        ls1.append('First list')
        ls2.append('Second list')

        #act
        ls1.extend(ls2)

        #assert
        self.assertEqual(ls1.get(1), 'Second list')

    def test__get_node(self):
        #arrange
        ls = linked_list.LinkedList()
        ls.append('2')
        ls.append('4')

        #act
        node = ls._get_node(1)

        #assert
        self.assertEqual(node.element, '4')

        with self.assertRaises(IndexError):
            ls._get_node(ls.get_length() + 2)


if __name__ == '__main__':
    unittest.main()