# ----Python Mini Project Management Library System----
# ----Create my_books.txt File----


import datetime
import os
os.getcwd()


class LMS():

    """
    This class is made for library management.
    The class has several functions, including displaying a list of books,
    the ability to borrow books, add books to the library, and return books.
    """
    # init function

    def __init__(self, list_of_books, library_name):
        self.list_of_books = list_of_books  # my_books
        self.library_name = library_name
        self.book_dict = {}
        Id = 101  # BookId
        with open(list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            # add content of my_books file to book_dict
            self.book_dict.update({str(Id): {"Book_title": line.replace("\n", ""),
                                             "Lender_name": "", "Issue_date": "", "Status": "Available"}})
            Id += 1
    # function for displaying books

    def display_books(self):
        print("------------------------List of Books---------------------")
        print("Book ID", "\t", "Title")
        print("----------------------------------------------------------")
        for key, value in self.book_dict.items():
            print(key, "\t\t", value.get("Book_title"),
                  "- [", value.get("Status"), "]")

    # lend books
    def Issue_books(self):
        book_id = input("please enter Book ID:")
        current_date = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")  # Record Book Delivery Time

        if book_id in self.book_dict.keys():  # Check Valid Id
            if not self.book_dict[book_id]["Status"] == "Available":
                print(f"this book is already Issueed to {self.book_dict[book_id]['Lender_name']} \
                    on {self.book_dict[book_id]['Issue_date']}")
                return self.Issue_books()
            elif self.book_dict[book_id]["Status"] == "Available":
                yourName = input("enter your name:")
                self.book_dict[book_id]["Lender_name"] = yourName
                self.book_dict[book_id]["Issue_date"] = current_date
                self.book_dict[book_id]['Status'] = 'Already Issued'
                print("Book Issued Successfuly !!!\n")
        else:
            print("Book ID Not Found")

    # add books
    def add_books(self):
        new_book = input("Enter Book Title: ")  # get book name
        if new_book == "":
            return self.add_books()
        elif len(new_book) > 25:  # Constraint for Length
            print("Book Title length is too long !!! Title length Should be less than 25")
            return self.add_books()
        else:
            with open(self.list_of_books, "a") as bk:  # Add Book Title to End of my_books File
                bk.writelines(f"{new_book}\n")
            self.book_dict.update({str(int(max(self.book_dict)+1)): {"Book_title": new_book,
                                                                     "Lender_name": "", "Issue_date": "", "Status": "Available"}})  # Add New Book To Dictionary
            print(f"{new_book} has been added successfuly")
    # return Books To Library

    def return_books(self):
        bookId = input("Enter Book ID:")  # Get Book Id
        if bookId in self.book_dict.keys():
            if self.book_dict[bookId]["Status"] == "Available":  # Check The Delivered Book
                print(
                    "This Book is already available in library ! Please Check your Book ID.")
                return self.return_books()
            elif self.book_dict[bookId]["Status"] != "Available":
                self.book_dict[bookId]["Lender_name"] = ""
                self.book_dict[bookId]["Issue_date"] = ""
                self.book_dict[bookId]["Status"] = "Available"
                print("Successfuly Updated !!!")
        else:
            print("Book Id is not Found")
            return self.return_books()


if __name__ == "__main__":
    try:
        myLms = LMS("my_books.txt", "Iman's")
        # Library Guide
        press_key_list = {"D": "Display Books", "I": "Issue Books",
                          "A": "Add Books", "R": "Return Books", "Q": "Quit"}

        key_press = False
        while (key_press != 'q'):
            print(
                f"\n--------------------Welcome To {myLms.library_name} Library----------------------")
            for key, value in press_key_list.items():
                print(f"Press {key} to {value}")
            key_press = input("Press key : ").lower()
            if key_press == "i":
                print("\nCurrent Selection : ISSUE BOOK\n")
                myLms.Issue_books()

            elif key_press == "a":
                print("\nCurrent Selection : ADD BOOK\n")
                myLms.add_books()

            elif key_press == "d":
                print("\nCurrent Selection : DISPLAY BOOKS\n")
                myLms.display_books()

            elif key_press == "r":
                print("\nCurrent Selection : RETURN BOOK\n")
                myLms.return_books()
            elif key_press == "q":
                break
            else:
                print("Something went wrong. Please check your input. !!!")
                continue
    except Exception as e:
        print("Something went wrong. Please check your input. !!!")
