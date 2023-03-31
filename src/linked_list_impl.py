class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def get_first(self):
        return self.head

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def add_first(self, data):
        new_node = Node(data, self.head)
        self.head = new_node

    def get(self, data):
        temp = self.head
        while temp:
            if temp.data == data:
                return temp
            else:
                temp = temp.next

        return None

    def get_last(self):
        temp = self.head
        while temp:
            if temp.next:
                temp = temp.next
            else:
                return temp

        return None

    def add(self, prev_data, data):

        prev_node = self.get(prev_data)
        if prev_node is None:
            raise ValueError("prev_node is None! Cannot add data to it!")

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def remove(self, data):
        temp = self.head
        if temp and temp.data == data:
            self.head = temp.next
            return True

        prev = None
        while temp:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return False

        prev.next = temp.next
        return True

    def size(self):
        temp = self.head
        counter = 0
        while temp:
            counter += 1
            temp = temp.next

        return counter

    def to_array(self):
        arr = list()
        temp = self.head
        while temp:
            arr.append(temp.data)
            temp = temp.next

        return arr


if __name__ == "__main__":
    linked_list = LinkedList()
    for value in range(5):
        linked_list.add_last(value)
    print(f"Linked list: {linked_list.to_array()}")
    # insert a node at the front
    linked_list.add_first(55)
    print(f"Linked list: {linked_list.to_array()}")
    # insert a node after a given node
    linked_list.add(3, 21)
    print(f"Linked list: {linked_list.to_array()}")
    print("-----------------------------")
    # this example was used to show both get_first() and get() methods
    linked_list.remove(55)
    if linked_list.get_first() == linked_list.get(0):
        print("Item 0 is the head of linked list")
    print(f"The length of linked list: {linked_list.size()}")
    print("-----------------------------")
    linked_list.remove(linked_list.get_last().data)
    print(f"The data of last node is {linked_list.get_last().data}")
    print(f"The length of linked list: {linked_list.size()}")
    print("-----------------------------")
    while linked_list.size() != 0:
        linked_list.remove(linked_list.get_first().data)

    if not linked_list.remove(0):
        print("Cannot be removed any item because of empty linked list!")

