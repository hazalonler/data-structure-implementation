class MyStack:
    def __init__(self):
        self.stack_list = []

    def __str__(self):
        return ", ".join(map(str, self.stack_list))

    def push(self, element):
        self.stack_list.append(element)

    def pop(self):
        self.stack_list.pop()

    def peek(self):
        return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def empty(self):
        return len(self.stack_list) == 0


if __name__ == "__main__":

    my_stack = MyStack()
    my_stack.push("apple")
    my_stack.push("orange")
    my_stack.push("strawberry")
    print(f"My stack file is [{my_stack.__str__()}]")
    print(f"Stack size: {my_stack.size()}")

    print(f"Is stack empty? {my_stack.empty()}")
    print(f"Top item: {my_stack.peek()}")
    my_stack.pop()
    print(f"Is stack empty? {my_stack.empty()}")
    print(f"Top item: {my_stack.peek()}")
    my_stack.pop()
    print(f"Top item: {my_stack.peek()}")
    my_stack.pop()
    print(f"Is stack empty? {my_stack.empty()}")


