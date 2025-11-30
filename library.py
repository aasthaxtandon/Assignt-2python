# Name : Aastha Tandon
# Roll No. : 2501201047
# Course : Problem Solving with Python
# Mini Project : Library Inventory & Borrowing System

# dictionaries to store data
books = {}      # example: {"B101": {"title": "Python", "author": "Guido", "copies": 5}}
borrowed = {}   # example: {"Amit": "B101"}


def add_book():
    print("\n--- ADD BOOK ---")
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    copies = int(input("Enter Number of Copies: "))

    books[book_id] = {
        "title": title,
        "author": author,
        "copies": copies
    }

    print("Book added.\n")


def view_books():
    print("\n--- VIEW BOOKS ---")
    if len(books) == 0:
        print("No books in library.\n")
        return

    print("BookID\tTitle\tAuthor\tCopies")
    print("------------------------------------------")
    for bid, info in books.items():
        print(f"{bid}\t{info['title']}\t{info['author']}\t{info['copies']}")
    print()


def search_book():
    print("\n--- SEARCH BOOK ---")
    print("1. Search by Book ID")
    print("2. Search by Title (substring)")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        bid = input("Enter Book ID: ")
        if bid in books:
            info = books[bid]
            print("Book Found:")
            print(f"ID: {bid}, Title: {info['title']}, Author: {info['author']}, Copies: {info['copies']}")
        else:
            print("Book Not Found.")
    elif choice == "2":
        key = input("Enter part of title: ").lower()
        found = False
        for bid, info in books.items():
            if key in info["title"].lower():
                if not found:
                    print("Books Found:")
                    found = True
                print(f"ID: {bid}, Title: {info['title']}, Author: {info['author']}, Copies: {info['copies']}")
        if not found:
            print("No book matched this title.")
    else:
        print("Wrong choice.")
    print()


def borrow_book():
    print("\n--- BORROW BOOK ---")
    student = input("Enter Student Name: ")
    bid = input("Enter Book ID: ")

    if bid not in books:
        print("Book ID does not exist.\n")
        return

    if books[bid]["copies"] <= 0:
        print("No copies left for this book.\n")
        return

    books[bid]["copies"] -= 1
    borrowed[student] = bid
    print(f"{student} borrowed book {bid}.\n")


def return_book():
    print("\n--- RETURN BOOK ---")
    student = input("Enter Student Name: ")
    bid = input("Enter Book ID: ")

    if student in borrowed and borrowed[student] == bid:
        books[bid]["copies"] += 1
        del borrowed[student]
        print("Book returned.\n")
    else:
        print("No such borrow record.\n")

    # list comprehension for borrowed list (as asked in assignment)
    borrowed_list = [f"{s} -> {b}" for s, b in borrowed.items()]
    print("Currently borrowed (student -> book):")
    print(borrowed_list)
    print()


def main():
    while True:
        print("====== LIBRARY MENU ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    print("Welcome to Library Inventory & Borrowing System\n")
    main()
