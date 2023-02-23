#!/usr/bin/env python3

class Shoe:

    def get_brand(self):
        return self._brand

    def __init__(self, brand, size=0):
        self.brand = brand
        self.size = size

    def set_size(self):
        return self._size

    def get_size(self, size):
        if (type(size) == int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
   

    size = property(set_size, get_size)