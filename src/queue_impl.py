class MyQueue:

    def __init__(self):
        self.queue = list()
        self.HEAD_INDEX = 0

    def __str__(self):
        return ", ".join(map(str, self.queue))

    def add(self, data):
        self.queue.append(data)
        return True

    def peek(self):
        return self.queue[self.HEAD_INDEX]

    def poll(self):
        if self.is_empty():
            return None

        return self.queue.pop(self.HEAD_INDEX)

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    new_queue = MyQueue()

    new_queue.add(75)
    new_queue.add("orange")
    new_queue.add("pineapple")

    print(f"Queue: [{new_queue.__str__()}]")
    print(f"Top item in queue is: {new_queue.peek()}")
    new_queue.poll()
    print(f"Is queue empty? {new_queue.is_empty()}")
    print(f"Top item in queue is: {new_queue.peek()}")
    new_queue.poll()
    print(f"Top item in queue is: {new_queue.peek()}")
    new_queue.poll()
    if new_queue.poll() is None:
        print("Cannot removed any item because of empty queue")



