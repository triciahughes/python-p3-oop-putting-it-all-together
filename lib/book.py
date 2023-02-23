#!/usr/bin/env python3

class Book:

    def title(self):
        return self.title

    def __init__(self, title, page_count=0):
        self.page_count = page_count
        self.title = title

    def author(self, author):
        self.author = author
    pass

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if (type(page_count) == int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")


    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

# title = property(title,)
    page_count = property(get_page_count, set_page_count,)
    # turn_page = property(get_turn_page, turn_page)
