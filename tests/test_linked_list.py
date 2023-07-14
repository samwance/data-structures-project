"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def test_insert_beginning(self):
        linked_list = LinkedList()
        linked_list.insert_beginning({'T': 1})
        linked_list.insert_beginning({'T': 2})
        linked_list.insert_beginning({'T': 3})
        self.assertEqual(str(linked_list), "{'T': 3} -> {'T': 2} -> {'T': 1} -> None")

    def test_insert_at_end(self):
        linked_list = LinkedList()
        linked_list.insert_at_end({'T': 1})
        linked_list.insert_at_end({'T': 2})
        linked_list.insert_at_end({'T': 3})
        self.assertEqual(str(linked_list), "{'T': 1} -> {'T': 2} -> {'T': 3} -> None")

if __name__ == "__main__":
    unittest.main()
