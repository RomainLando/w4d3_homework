import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author_repository.delete_all()
book_repository.delete_all()

author1 = Author("John", "Tolkien")
book11 = Book("The Silmarillion", author1)
book12 = Book("The Hobbit", author1)

author2= Author("Howard", "Lovecraft")
book21 = Book("The Call of Cathulu", author2)
book22 = Book("Necronomicon", author2)

author_repository.save(author1)
author_repository.save(author2)

print(author_repository.select_all())

book_repository.save(book11)
book_repository.save(book12)
book_repository.save(book21)
book_repository.save(book22)

print(book_repository.select_all())