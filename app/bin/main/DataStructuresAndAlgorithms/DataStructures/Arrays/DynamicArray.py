#!/usr/bin/env python3

class Array():

    ar = []      # Pretend this is actually a static array
    size = 0     # length user thinks array is
    capacity = 0  # Actual array size

    def __init__(self, capacity=16):
        if capacity <= 0:
            raise ValueError("Illegal size.")
        self.ar = [None for _ in range(capacity)]
        self.capacity = capacity
        self.iter_index = 0

    def is_empty(self):
        return self.size == 0

    def clear(self):
        for i in range(self.size):
            self.ar[i] = None
        self.size = 0

    def add(self, elem):

        # Time to resize!
        if self.size + 1 == self.capacity:

            self.capacity *= 2

            new_ar = [None for _ in range(self.capacity)]
            new_ar[:self.size] = self.ar[:self.size]
            self.ar = new_ar

        self.ar[self.size] = elem
        self.size = self.size + 1

    # Removes an element at a specified index
    def remove_at(self, i):

        if i < 0 or i >= self.size:
            raise IndexError("remove_at index out of bounds")
        data = self.ar[i]

        new_ar = [None for _ in range(self.size-1)]
        new_ar[:i] = self.ar[:i]
        new_ar[i:] = self.ar[i+1:]

        self.capacity = self.size = self.size - 1
        return data

    def remove(self, obj):

        index = self.index_of(obj)
        if index == -1:
            return False

        self.remove_at(index)
        return True

    def index_of(self, obj):

        for i in range(self.size):
            if obj == None:
                if self[i] == None:
                    return i
            else:
                if obj.__eq__(self.ar[i]):
                    return i
        return -1

    # Allows you to treat this class as an array and set values
    # via the square bracket notation like: myarray[index] = someobject
    def __setitem__(self, index, item):
        if index < 0 or index >= self.size:
            raise IndexError("Remove index out of bounds")
        self.ar[index] = item

    # Allows you to treat this class as an array and get values
    # via the square bracket notation like: someobject = myarray[index]
    def __getitem__(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Get index out of bounds")
        return self.ar[index]

    # Overrides the 'in' keyword to easily check if
    # an element is contained within this array
    def __contains__(self, obj):
        return self.index_of(obj) != -1

    # Overrides the 'len' builtin to return the size of this array
    def __len__(self):
        return self.size

    # Returns an iterator for this array. Allows for-in loop.
    def __iter__(self):
        self.iter_index = 0
        return self

    def __next__(self):

        if self.iter_index == self.size:
            raise StopIteration()

        data = self[self.iter_index]
        self.iter_index = self.iter_index + 1
        return data

    # Returns a string representation of this array
    def __str__(self):
        return "[" + ', '.join(map(str, self[:self.size])) + "]"
