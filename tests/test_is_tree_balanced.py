import unittest
from src.is_tree_balanced import BinaryTree, is_tree_balanced


class Test(unittest.TestCase):

    def test_1_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)

        self.assertEqual(is_tree_balanced(root), True)

    def test_2_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(8)
        root.right.right = BinaryTree(10)
        root.left.left = BinaryTree(3)
        root.left.left.left = BinaryTree(4)
        root.left.left.right = BinaryTree(5)
        root.left.right = BinaryTree(6)
        root.left.right.right = BinaryTree(7)
        root.right.right.right = BinaryTree(11)
        root.right.left = BinaryTree(9)

        self.assertEqual(is_tree_balanced(root), True)

    def test_1_not_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(8)
        root.right.right = BinaryTree(10)
        root.left.left = BinaryTree(3)
        root.left.left.left = BinaryTree(4)
        root.left.left.right = BinaryTree(5)
        root.left.right = BinaryTree(6)
        root.left.right.right = BinaryTree(7)
        root.right.right.right = BinaryTree(11)

        self.assertEqual(is_tree_balanced(root), False)

    def test_2_not_balanced_tree(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.right = BinaryTree(3)
        root.left.left = BinaryTree(4)
        root.left.right = BinaryTree(5)
        root.left.left.left = BinaryTree(6)

        self.assertEqual(is_tree_balanced(root), False)

    def test_one_element_tree(self):
        root = BinaryTree(1)

        self.assertEqual(is_tree_balanced(root), True)


if __name__ == '__main__':
    unittest.main()
