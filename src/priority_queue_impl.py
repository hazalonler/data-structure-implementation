from linked_list_impl import LinkedList


class PriorityData:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __str__(self):
        return f"PriorityData({self.value}, {self.priority})"


class MyPriorityQueue:
    def __init__(self):
        self.queue = LinkedList()

    def is_empty(self):
        if self.queue.head is None:
            return True
        else:
            return False

    def add(self, value, priority):
        new_element = PriorityData(value, priority)

        if self.queue.head is None:
            self.queue.add_first(new_element)
        else:
            if priority > self.queue.head.data.priority:
                self.queue.add_first(new_element)
            else:
                temp = self.queue.head
                while temp.next:
                    if priority >= temp.next.data.priority:
                        break
                    temp = temp.next
                self.queue.add(temp.data, new_element)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue.head

    def poll(self):
        if self.is_empty():
            return None
        else:
            removed_elem = self.queue.head.data
            self.queue.remove(removed_elem)

            return removed_elem

    def to_array(self):
        arr = list()
        temp = self.queue.head
        while temp:
            arr.append(temp.data.value)
            temp = temp.next

        return arr


if __name__ == "__main__":
    priority_queue = MyPriorityQueue()
    print("Adding elements with different priority!")
    priority_queue.add(10, 1)
    priority_queue.add(12, 3)
    priority_queue.add(14, 2)
    priority_queue.add(16, 2)
    priority_queue.add(10, 3)

    print(priority_queue.to_array())

    print(priority_queue.poll())
    print(priority_queue.to_array())
    head_value = priority_queue.peek()
    print(head_value.data)
    priority_queue.poll()
    print(priority_queue.to_array())
    head_value = priority_queue.peek()
    print(head_value.data)





