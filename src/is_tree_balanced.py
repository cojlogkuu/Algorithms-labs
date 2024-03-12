def to_bool(func):
    def wrapper(*args, **kwargs):
        if 'recursive' in kwargs and kwargs['recursive']:
            return func(*args, **kwargs)
        else:
            return bool(func(*args, **kwargs))

    return wrapper


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @classmethod
    @to_bool
    def is_tree_balanced(cls, node, *args, **kwargs):
        if not node:
            return 1

        left_height, right_height = cls.is_tree_balanced(node.left, recursive=True), cls.is_tree_balanced(node.right,
                                                                                                          recursive=True)

        if not left_height or not right_height or abs(left_height - right_height) > 1:
            return False
        else:
            return max(left_height, right_height) + 1
