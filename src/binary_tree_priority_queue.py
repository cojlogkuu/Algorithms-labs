class Node:
    def __init__(self, data, priority, left=None, right=None):
        self.data = data
        self.priority = priority
        self.left = left
        self.right = right


class BinaryTreeQueue:
    def __init__(self):
        self.root = None

    def __find_place_for_element_to_put(self, priority, node):
        if priority <= node.priority:
            if node.left:
                return self.__find_place_for_element_to_put(priority, node.left)
            else:
                return node, True
        elif priority > node.priority:
            if node.right:
                return self.__find_place_for_element_to_put(priority, node.right)
            else:
                return node, False

    def __get_position_of_element(self, priority, node, parent=None):
        if not node:
            return None, None

        if priority == node.priority:
            return node, parent

        if priority < node.priority:
            return self.__get_position_of_element(priority, node.left, node)
        elif priority > node.priority:
            return self.__get_position_of_element(priority, node.right, node)

    def __get_min_recursive(self, node, parent=None):
        if not node.left:
            return node.priority, node, parent
        return self.__get_min_recursive(node.left, node)

    def __delete_leaf(self, node, parent):
        if parent.left is node:
            parent.left = None
        elif parent.right is node:
            parent.right = None

    def __delete_one_child(self, parent, node, child):
        if parent.left is node:
            parent.left = child
        elif parent.right is node:
            parent.right = child

    def __delete_two_child(self, node):
        min_element, min_node, min_parent = self.__get_min_recursive(node.right, node)
        node.data = min_node.data
        node.priority = min_node.priority

        if not min_node.left and not min_node.right:
            self.__delete_leaf(min_node, min_parent)

        elif not min_node.left and min_node.right:
            self.__delete_one_child(min_parent, min_node, min_node.right)

    def __delete_root(self):
        if not self.root.right:
            self.root = self.root.left
        else:
            self.__delete_two_child(self.root)

    def add_element(self, element, priority):
        if not self.root:
            self.root = Node(element, priority)
            return

        parent, is_left = self.__find_place_for_element_to_put(priority, self.root)

        if is_left:
            parent.left = Node(element, priority)
        else:
            parent.right = Node(element, priority)

    def __delete_element(self, priority):
        if priority == self.root.priority:
            self.__delete_root()
            return

        node, parent = self.__get_position_of_element(priority, self.root)

        if not node.left and not node.right:
            self.__delete_leaf(node, parent)
            return

        if node.left and not node.right:
            self.__delete_one_child(parent, node, node.left)
            return
        elif not node.left and node.right:
            self.__delete_one_child(parent, node, node.right)
            return

        if node.left and node.right:
            self.__delete_two_child(node)
            return

    def get_next_task(self):
        if not self.root:
            return None
        _, node, _ = self.__get_min_recursive(self.root)
        self.__delete_element(node.priority)
        return node.data

    def get_queue(self):
        def sorted_recursive(node):
            if node:
                sorted_recursive(node.left)
                result_arr.append(node.data)
                sorted_recursive(node.right)

        node = self.root
        result_arr = []
        sorted_recursive(node)
        return result_arr
