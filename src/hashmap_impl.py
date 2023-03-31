class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class MyHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.element_size = 0
        self.load_factor = 0.75
        self.list = [None] * self.capacity

    def __str__(self):
        pair_list = list()
        for key in self.keys():
            value = self.get(key)
            pair_list.append((key, value))

        return f"HashTable: {pair_list}"

    def __hash_code(self, key):
        if key is None:
            raise BaseException("'key' should not be none!")

        total = 0
        constant_prime = 31
        for char in repr(key).lstrip("'"):
            total += (ord(char) * constant_prime)

        return total % self.capacity

    def __load_check(self):
        return self.element_size / self.capacity > self.load_factor

    def __resize_if_necessary(self):
        if not self.__load_check():
            return

        new_hash_table = MyHashTable(self.capacity * 2)
        for node in self.list:
            temp = node
            while temp:
                new_hash_table.put(temp.key, temp.value)
                temp = temp.next

        self.capacity = new_hash_table.capacity
        self.list = new_hash_table.list

    def size(self):
        return self.element_size

    def keys(self):
        keys = list()
        for node in self.list:
            temp = node
            while temp:
                keys.append(temp.key)
                temp = temp.next
        return keys

    def values(self):
        values = list()
        for node in self.list:
            temp = node
            while temp:
                values.append(temp.value)
                temp = temp.next

        return values

    def contains_key(self, key):
        if self.get(key):
            return True

        return False

    def get_or_default(self, key, default_value):
        maybeValue = self.get(key)
        if maybeValue is not None:
            return maybeValue

        return default_value

    def put_if_absent(self, key, value):
        maybeValue = self.get(key)
        if maybeValue is not None:
            return maybeValue

        self.put(key, value)

    def put(self, key, value):
        self.__resize_if_necessary()

        node = Node(key, value)
        hash_code = self.__hash_code(key)
        if self.list[hash_code] is None:
            self.list[hash_code] = node
            self.element_size += 1
            return value

        temp = self.list[hash_code]
        while temp:
            if temp.key == key:
                temp.value = value
                return value

            if temp.next is None:
                temp.next = node
                self.element_size += 1
                return value

            temp = temp.next

    def get(self, key):
        temp = self.list[self.__hash_code(key)]
        while temp:
            if temp.key == key:
                return temp.value
            temp = temp.next

        return None

    def remove(self, key):
        index = self.__hash_code(key)
        temp = self.list[index]
        if temp is None:
            return None

        prev = None
        while temp:
            if temp.key == key:
                break

            prev = temp
            temp = temp.next

        if temp:
            self.element_size -= 1
            if prev:
                prev.next = temp.next
            else:
                self.list[index] = temp.next

            return temp.value

        return None


if __name__ == "__main__":
    my_hashtable = MyHashTable()
    my_hashtable.put("Hazal", 2)
    my_hashtable.put("hazal", 4)
    my_hashtable.put(1556, 7)
    my_hashtable.put("1556", 3)
    my_hashtable.put("HAZAL", 5)
    my_hashtable.put("LAZAH", 8)

    print(f"The hash table: {my_hashtable}")
    my_hashtable.put("HAZAL", 10)
    print(f"The hash table: {my_hashtable}")

    print(f"Removal key value pair ('1556',{my_hashtable.remove('1556')})")

    print(f"The value of 'HAZAL' or 0: {my_hashtable.get_or_default('HAZAL', 0)}")

    print(f"The value: {my_hashtable.put_if_absent('Hazal', 25)}")

    print(f"\nThe keys: {my_hashtable.keys()}")

    print(f"\nThe values: {my_hashtable.values()}")

    size = my_hashtable.size()
    print(f"\nThe size of hash table: {size}")

    if my_hashtable.contains_key(1556):
        print("Hashtable contains this key")
    else:
        print("This key cannot be found")


