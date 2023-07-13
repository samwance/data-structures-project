"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()


    def test_str(self):
        self.queue.enqueue('1')
        self.queue.enqueue('2')
        self.queue.enqueue('3')
        self.assertEqual(str(self.queue), 'Queue: 1, 2, 3')


    def test_enqueue(self):
        self.queue.enqueue('1')
        self.queue.enqueue('2')
        self.queue.enqueue('3')
        self.assertEqual(self.queue.head.data, '1')
        self.assertEqual(self.queue.tail.data, '3')


    def test_dequeue(self):
        self.queue.enqueue('1')
        self.queue.enqueue('2')
        self.queue.enqueue('3')
        self.assertEqual(self.queue.dequeue(), '1')
        self.assertEqual(self.queue.dequeue(), '2')
        self.assertEqual(self.queue.dequeue(), '3')
        self.assertEqual(self.queue.dequeue(), None)
