class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    
    def describe(self):
        print(f"'{self.title}' by {self.author}, published in {self.year_published}.")

book1 = Book("Pride and Prejudice", "Jane Austen", 1813)
book2 = Book("Moby-Dick", "Herman Melville", 1851)
book3 = Book("The Catcher in the Rye", "J.D. Salinger", 1951)

# Displaying book details
book1.describe()
book2.describe()
book3.describe()