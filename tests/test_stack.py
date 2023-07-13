"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()


    def test_str(self):
        self.assertEqual(str(self.stack), "Stack is empty")
        self.stack.push('1')
        self.stack.push('2')
        self.stack.push('3')
        self.assertEqual(str(self.stack), 'Stack: 3, 2, 1')


    def test_push(self):
        self.stack.push('1')
        self.stack.push('2')
        self.stack.push('3')
        self.assertEqual(self.stack.top.data, '3')
        self.assertEqual(self.stack.top.next_node.data, '2')
        self.assertEqual(self.stack.top.next_node.next_node.data, '1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)


    def test_pop(self):
        self.stack.push('1')
        data = self.stack.pop()
        self.assertEqual(data, '1')
