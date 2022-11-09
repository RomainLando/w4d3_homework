class Book:
    def __init__(self, title, author, id=None):
        self.title = title
        self.author = author
        self.id = id
    
    def __str__(self):
        return f"{self.title} by {self.author.first_name} {self.author.last_name}"