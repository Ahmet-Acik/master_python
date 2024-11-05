# library_management.py
"""
Library Management System

This module uses lists, sets, tuples, and dictionaries to manage library data. 
It includes comprehensive business logic and demonstrates the use of common methods for each data structure.

Data Structures:

1. Lists: To store collections of books and users.
2. Tuples: To store immutable book details.
3. Sets: To manage unique genres.
4. Dictionaries: To map book titles to their details and manage user checkouts.

List of books in the library with genres:
books = [
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ...
]

List of users:
users = ["Alice", "Bob", "Charlie", "Diana"]

Set of unique genres:
genres = set()

Adding genres from books:
for book in books:
    genres.add(book[3])

Dictionary to map book titles to their details:
library_catalog = {title: (author, year, genre) for title, author, year, genre in books}

Dictionary to manage user checkouts:
user_checkouts = {user: [] for user in users}

Assign books to genres:
for book in books:
    genres.add(book[3])

Functions:

List-Related Methods:
1. find_book_index(title): Finds the index of a book in the list.
2. sort_books_by_year(): Sorts books by year.
3. reverse_users(): Reverses the list of users.
4. append_user(user): Appends a new user to the list.
5. remove_user(user): Removes a user from the list.

Tuple-Related Methods:
1. find_max_min_year(): Finds the maximum and minimum year of books.

Set-Related Methods:
1. add_genre(genre): Adds a new genre.
2. remove_genre(genre): Removes a genre.
3. list_all_genres(): Lists all genres.
4. find_common_genres(other_genres): Finds common genres between two sets.
5. find_unique_genres(): Finds unique genres in the library.
6. clear_genres(): Clears all genres.

Dictionary-Related Methods:
1. add_book(title, author, year, genre): Adds a new book to the library.
2. remove_book(title): Removes a book from the library.
3. get_book_details(title): Gets book details.
4. list_books_by_author(author): Lists all books by an author.
5. list_books_by_genre(genre): Lists all books in a genre.
6. count_books_by_author(author): Counts books by an author.
7. checkout_book(user, book_title): Checks out a book to a user.
8. return_book(user, book_title): Returns a book from a user.
9. update_book_details(title, new_details): Updates book details.
10. merge_library_catalogs(other_catalog): Merges two library catalogs.
11. get_all_book_titles(): Gets all book titles.
12. clear_library_catalog(): Clears the library catalog.

"""
# List of books in the library with genres
books = [
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Science Fiction"),
    ("Pride and Prejudice", "Jane Austen", 1813, "Classic"),
    ("The Catcher in the Rye", "J.D. Salinger", 1951, "Fiction"),
    ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy"),
    ("Fahrenheit 451", "Ray Bradbury", 1953, "Science Fiction"),
    ("Jane Eyre", "Charlotte Brontë", 1847, "Classic"),
    ("Wuthering Heights", "Emily Brontë", 1847, "Classic"),
    ("The Road", "Cormac McCarthy", 2006, "Fiction"),
    ("Beloved", "Toni Morrison", 1987, "Fiction"),
    ("The Goldfinch", "Donna Tartt", 2013, "Fiction"),
    ("The Underground Railroad", "Colson Whitehead", 2016, "Fiction"),
    ("A Visit from the Goon Squad", "Jennifer Egan", 2010, "Fiction"),
    ("Day of the Oprichnik", "Vladimir Sorokin", 2006, "Science Fiction"),
    ("The Light and the Dark", "Mikhail Shishkin", 2013, "Fiction"),
    ("The Big Green Tent", "Ludmila Ulitskaya", 2010, "Fiction"),
    ("Laurus", "Eugene Vodolazkin", 2012, "Historical Fiction"),
    ("The Aviator", "Eugene Vodolazkin", 2016, "Historical Fiction"),
    ("The Notebook", "Nicholas Sparks", 1996, "Romance"),
    ("Pride and Prejudice", "Jane Austen", 1813, "Romance"),
    ("The Fault in Our Stars", "John Green", 2012, "Romance"),
    ("Me Before You", "Jojo Moyes", 2012, "Romance"),
    ("The Rosie Project", "Graeme Simsion", 2013, "Romance"),
    ("The Rosie Effect", "Graeme Simsion", 2014, "Romance"),
    ("The Rosie Result", "Graeme Simsion", 2019, "Romance"),
    ("The Time Traveler's Wife", "Audrey Niffenegger", 2003, "Romance"),
    ("Outlander", "Diana Gabaldon", 1991, "Romance"),
    ("The Thorn Birds", "Colleen McCullough", 1977, "Romance"),
]

# List of users
users = ["Alice", "Bob", "Charlie", "Diana"]

# Set of unique genres
genres = set()

# Adding genres from books
for book in books:
    title, author, year, genre = book
    genres.add(genre)

# Dictionary to map book titles to their details
library_catalog = {title: (author, year, genre) for title, author, year, genre in books}

# Dictionary to manage user checkouts
user_checkouts = {user: [] for user in users}


# Function to checkout a book
def checkout_book(user, book_title):
    if book_title in library_catalog and user in user_checkouts:
        user_checkouts[user].append(book_title)
        print(f"{user} checked out {book_title}.")
    else:
        print(f"Book or user not found.")


# Function to return a book
def return_book(user, book_title):
    if user in user_checkouts and book_title in user_checkouts[user]:
        user_checkouts[user].remove(book_title)
        print(f"{user} returned {book_title}.")
    else:
        print(f"Book or user not found.")


# Function to get book details
def get_book_details(book_title):
    return library_catalog.get(book_title, "Book not found.")


# Function to list all books by an author
def list_books_by_author(author):
    return [title for title, details in library_catalog.items() if details[0] == author]


# Function to list all books in a genre
def list_books_by_genre(genre):
    return [title for title, details in library_catalog.items() if details[2] == genre]


# Function to count books by an author
def count_books_by_author(author):
    return sum(1 for title, details in library_catalog.items() if details[0] == author)


# Function to find the index of a book in the list
def find_book_index(book_title):
    for index, book in enumerate(books):
        if book[0] == book_title:
            return index
    return -1


# Function to add a new genre
def add_genre(genre):
    genres.add(genre)
    print(f"Genre '{genre}' added.")


# Function to remove a genre
def remove_genre(genre):
    genres.discard(genre)
    print(f"Genre '{genre}' removed.")


# Function to list all genres
def list_all_genres():
    return genres


# Function to sort books by year
def sort_books_by_year():
    return sorted(books, key=lambda book: book[2])


# Function to reverse the list of users
def reverse_users():
    return users[::-1]


# Function to find the maximum and minimum year of books
def find_max_min_year():
    years = [book[2] for book in books]
    return max(years), min(years)


# Function to count the occurrences of a specific author
def count_author_occurrences(author):
    return sum(1 for book in books if book[1] == author)


# Function to find common genres between two sets
def find_common_genres(other_genres):
    return genres.intersection(other_genres)


# Function to find unique genres in the library
def find_unique_genres():
    return genres.difference({"Fiction", "Classic"})


# Function to update book details
def update_book_details(book_title, new_details):
    if book_title in library_catalog:
        library_catalog[book_title] = new_details
        print(f"Updated details for {book_title}.")
    else:
        print(f"Book {book_title} not found.")


# Function to merge two library catalogs
def merge_library_catalogs(other_catalog):
    library_catalog.update(other_catalog)
    print("Library catalogs merged.")


# Function to append a new book to the list
def append_book(book):
    books.append(book)
    print(f"Book '{book[0]}' added.")


# Function to remove a user from the list
def remove_user(user):
    if user in users:
        users.remove(user)
        print(f"User '{user}' removed.")
    else:
        print(f"User '{user}' not found.")


# Function to clear all genres
def clear_genres():
    genres.clear()
    print("All genres cleared.")


# Function to get all book titles
def get_all_book_titles():
    return list(library_catalog.keys())


# Function to clear the library catalog
def clear_library_catalog():
    library_catalog.clear()
    print("Library catalog cleared.")


# Example usage
if __name__ == "__main__":
    print("Library Catalog:")
    for title, details in library_catalog.items():
        print(f"{title}: {details}")

    print("\nGenres Available:")
    print(genres)

    print("\nUser Checkouts:")
    for user, checkouts in user_checkouts.items():
        print(f"{user}: {checkouts}")

    # Checkout and return books
    checkout_book("Alice", "1984")
    checkout_book("Bob", "The Great Gatsby")
    return_book("Alice", "1984")

    print("\nUser Checkouts After Transactions:")
    for user, checkouts in user_checkouts.items():
        print(f"{user}: {checkouts}")

    # Get book details
    print("\nBook Details:")
    print(get_book_details("1984"))

    # List books by author
    print("\nBooks by George Orwell:")
    print(list_books_by_author("George Orwell"))

    # Count books by author
    print("\nCount of books by George Orwell:")
    print(count_books_by_author("George Orwell"))

    # Find book index
    print("\nIndex of '1984':")
    print(find_book_index("1984"))

    # Add and remove genres
    add_genre("Mystery")
    remove_genre("Romance")

    # List all genres
    print("\nAll Genres:")
    print(list_all_genres())

    # Sort books by year
    print("\nBooks Sorted by Year:")
    for book in sort_books_by_year():
        print(book)

    # Reverse the list of users
    print("\nReversed List of Users:")
    print(reverse_users())

    # Find the maximum and minimum year of books
    max_year, min_year = find_max_min_year()
    print(f"\nMaximum Year: {max_year}, Minimum Year: {min_year}")

    # Count the occurrences of a specific author
    print(
        f"\nOccurrences of 'George Orwell': {count_author_occurrences('George Orwell')}"
    )

    # Find common genres between two sets
    other_genres = {"Fiction", "Mystery", "Adventure"}
    print(f"\nCommon Genres: {find_common_genres(other_genres)}")

    # Find unique genres in the library
    print(f"\nUnique Genres: {find_unique_genres()}")

    # Update book details
    update_book_details("1984", ("George Orwell", 1949, "Dystopian"))
    print(f"\nUpdated Book Details: {get_book_details('1984')}")

    # Merge two library catalogs
    other_catalog = {
        "Brave New World": ("Aldous Huxley", 1932, "Dystopian"),
        "The Handmaid's Tale": ("Margaret Atwood", 1985, "Dystopian"),
    }
    merge_library_catalogs(other_catalog)
    print("\nMerged Library Catalog:")
    for title, details in library_catalog.items():
        print(f"{title}: {details}")

    # Append a new book to the list
    new_book = ("The Alchemist", "Paulo Coelho", 1988, "Fiction")
    append_book(new_book)
    print("\nUpdated List of Books:")
    for book in books:
        print(book)

    # Remove a user from the list
    remove_user("Charlie")
    print("\nUpdated List of Users:")
    print(users)

    # Clear all genres
    clear_genres()
    print("\nGenres After Clearing:")
    print(genres)

    # Get all book titles
    print("\nAll Book Titles:")
    print(get_all_book_titles())

    # Clear the library catalog
    clear_library_catalog()
    print("\nLibrary Catalog After Clearing:")
    print(library_catalog)
