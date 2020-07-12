
class Book:

    def __init__(self, title, author, num_pages, current_page):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.current_page = current_page
        self.bookmarked_page = 1


    def move_bookmark(self, page=None):
        if not page:
            self.bookmarked_page = self.current_page
        else:
            self.bookmarked_page = page

    def go_to_page(self, page):
        self.current_page = page      

    def turn_page(self, forward):
        if forward:
            self.current_page += 1
            if self.current_page > self.num_pages:
                self.current_page = 1
        else:
            self.current_page -= 1

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}"

    def __len__(self):
        return self.num_pages



book_1 = Book("Cats", "Real Person", 213, 212)
print(book_1.current_page)
book_1.turn_page(True)
print(book_1.current_page)
book_1.turn_page(True)
print(book_1.current_page)

book_1.go_to_page(75)
book_1.move_bookmark(120)
print(book_1.current_page)
print(book_1.bookmarked_page)
