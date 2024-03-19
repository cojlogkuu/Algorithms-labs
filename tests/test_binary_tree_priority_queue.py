import unittest
from src.binary_tree_priority_queue import BinaryTreeQueue


class Test(unittest.TestCase):

    def test_add_to_queue(self):
        queue = BinaryTreeQueue()
        arr = [('t1', 5), ('t2', 4), ('t3', 3), ('t4', 6), ('t5', 2), ('t6', 1), ('t7', 8), ('t8', 7)]
        for i, j in arr:
            queue.add_element(i, j)

        queue_list = queue.get_queue()

        self.assertEqual(queue_list, ['t6', 't5', 't3', 't2', 't1', 't4', 't8', 't7'])

    def test_empty_queue(self):
        queue = BinaryTreeQueue()
        queue_list = queue.get_queue()
        queue_next_task = queue.get_next_task()

        self.assertEqual(queue_list, [])
        self.assertEqual(queue_next_task, None)

    def test_get_next_task(self):
        queue = BinaryTreeQueue()
        arr = [('t1', 5), ('t2', 4), ('t3', 3), ('t4', 6), ('t5', 2), ('t6', 1), ('t7', 8), ('t8', 7)]
        for i, j in arr:
            queue.add_element(i, j)

        task1 = queue.get_next_task()
        self.assertEqual(task1, 't6')
        task2 = queue.get_next_task()
        self.assertEqual(task2, 't5')

        queue_list = queue.get_queue()
        self.assertEqual(queue_list, ['t3', 't2', 't1', 't4', 't8', 't7'])


if __name__ == '__main__':
    unittest.main()
