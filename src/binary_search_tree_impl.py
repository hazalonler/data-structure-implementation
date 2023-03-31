class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.key = key


class MyBinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.__do_insert(key, self.root)

    def __do_insert(self, key, node):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self.__do_insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self.__do_insert(key, node.right)

    def search(self, key):
        return self.__do_search(key, self.root)

    def __do_search(self, key, node):
        if node is None:
            return None

        if key == node.key:
            return node

        if key > node.key:
            return self.__do_search(key, node.right)

        if key < node.key:
            return self.__do_search(key, node.left)

    def __left_most(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, key):
        self.root = self.__delete(key, self.root)

    def __delete(self, key, node):
        if node is None:
            return None

        if key < node.key:
            node.left = self.__delete(key, node.left)
        elif key > node.key:
            node.right = self.__delete(key, node.right)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            left_most = self.__left_most(node.right)
            node.key = left_most.key

            node.right = self.__delete(left_most.key, node.right)
        return node

    def preorder_traversal(self):
        self.__preorder_traversal(self.root)

    def __preorder_traversal(self, node):
        if node:
            print(node.key, end=" ")
            self.__preorder_traversal(node.left)
            self.__preorder_traversal(node.right)

    def inorder_traversal(self):
        self.__inorder_traversal(self.root)

    def __inorder_traversal(self, focus_node):
        if focus_node is not None:
            self.__inorder_traversal(focus_node.left)
            print(focus_node.key, end=" ")
            self.__inorder_traversal(focus_node.right)

    def postorder_traversal(self):
        self.__postorder_traversal(self.root)

    def __postorder_traversal(self, focus_node):
        if focus_node:
            self.__postorder_traversal(focus_node.left)
            self.__postorder_traversal(focus_node.right)
            print(focus_node.key, end=" ")


if __name__ == '__main__':
    my_tree = MyBinarySearchTree()
    my_tree.insert(20)
    my_tree.insert(30)

    my_tree.delete(20)
    print("\nInorder Traversal of my tree: ")
    my_tree.inorder_traversal()

    my_tree.insert(15)
    my_tree.insert(65)
    my_tree.insert(45)
    my_tree.insert(5)
    my_tree.insert(25)

    print("\nInorder Traversal of my tree: ")
    my_tree.inorder_traversal()

    searched_node = my_tree.search(65)
    print("\nThis is the searched number: {}".format(searched_node.key))

    my_tree.insert(26)
    print("\nInorder Traversal of my tree: ")
    my_tree.inorder_traversal()

    my_tree.delete(30)
    print("\nInorder Traversal of my tree: ")
    my_tree.inorder_traversal()

    my_tree.delete(65)
    print("\nInorder Traversal of my tree: ")
    my_tree.inorder_traversal()

    my_tree.delete(5)
    print("\nInorder Traversal of my tree: ")
    my_tree.inorder_traversal()


