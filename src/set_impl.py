from src.hashmap_impl import MyHashTable


class MySet:
    def __init__(self):
        self.set = MyHashTable()

    def __str__(self):
        set_list = list()
        for key in self.set.keys():
            set_list.append(key)

        return f"{set_list}"

    def add(self, key):
        added_value = self.set.put_if_absent(key, value=None)

        return added_value is None

    def remove(self, key):
        removed_value = self.set.remove(key)

        return removed_value is not None

    def is_empty(self):
        return self.set.size() == 0

    def contains(self, key):
        return self.set.contains_key(key)

    def size(self):
        return self.set.size()


if __name__ == "__main__":

    mySet = MySet()
    mySet.add("apple")
    mySet.add("orange")
    mySet.add("blueberry")

    print(f"Set {mySet}")

    mySet.remove("apple")
    print(f"Set {mySet}")
    print(f"Set size: {mySet.size()}")

    mySet.remove("orange")
    print(f"Is set not empty: {not mySet.is_empty()}")
    print(f"Does set contain 'orange': {mySet.contains('orange')}")

    mySet.remove("blueberry")
    print(f"Is set empty: {mySet.is_empty()}")




