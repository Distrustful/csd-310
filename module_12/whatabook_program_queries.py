#Import Statements
import os
import mysql.connector
from mysql.connector import errorcode

#-----termclear() method-----
def termclear():
    os.system('cls')

#Menu Methods:
#-----show_menu() method-----
def show_menu():
    print("--- MAIN MENU ---")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")

    userinput = input("\nMenu Option: ")

    #Check User Entry
    if userinput == ('1'):
        termclear()
        show_books(cursor)
    elif userinput == ('2'):
        termclear()
        show_locations(cursor)
    elif userinput == ('3'):
        termclear()
        validate_user(cursor)
    else:
        termclear()
        print("Please Choose Valid Menu Option\n")
        show_menu()
#-----show_account_menu() method-----
def show_account_menu(cursor, userid):
    #GET first_name and last_name FROM user
    cursor.execute("SELECT first_name, last_name FROM user WHERE user_id = %s", (userid,))

    username = cursor.fetchall()

    #Display Account Menu
    for user in username:

        print("--- ACCCOUNT MENU ---")
        #Display Users First And Last Name
        print("Welcome {}".format(user[0]+ " {}".format(user[1])))
        print("1. Wishlist")
        print("2. Add Book")
        print("3. Return to Main Menu\n")

        userinput = input("Menu Option: ")
        
        #Check User Input
        if userinput == '1':
            termclear()
            show_wishlist(cursor, userid)

        elif userinput == '2':
            termclear()
            show_books_to_add(cursor, userid)

        elif userinput == '3':
            termclear()
            show_menu()
        else:
            termclear()
            print("Please Choose Valid Menu Option\n")
            show_account_menu(cursor, userid)

#Menu Check Methods:
#-----main_menu_check() method-----
def main_menu_check():
#Check if user wants to go back to main menu
        userinput = input("Return to main menu? (Y/N): ")
        if userinput == 'Y' or userinput == 'y':
            termclear()
            show_menu()
        elif userinput == 'N' or userinput == 'n':
            termclear()
            print("Quitting...")
            db.close
        else:
            termclear()
            print("Please Enter Valid Option:")
            main_menu_check()
#-----account_menu_check() method-----
def account_menu_check(cursor, userid):
#Check if user wants to go back to account menu
        userinput = input("\nReturn to account menu? (Y/N): ")
        if userinput == 'Y' or userinput == 'y':
            termclear()
            show_account_menu(cursor, userid)
        elif userinput == 'N' or userinput == 'n':
            termclear()
            print("Quitting...")
            db.close
        else:
            termclear()
            print("Please Enter Valid Option:")
            account_menu_check(cursor, userid)

#Show Methods
#-----show_books() method-----
def show_books(cursor):

    #Display books code
    cursor.execute("SELECT book_id, book_name, author, details FROM book")

    books = cursor.fetchall()

    print("-- DISPLAYING BOOKS --")
    for book in books:
        print("Book ID: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Author: {}".format(book[2]))
        print("Details: {}".format(book[3]) + "\n")

    main_menu_check()
#-----show_locations() method-----
def show_locations(cursor):
    cursor.execute("SELECT store_id, locale FROM store")

    stores = cursor.fetchall()
    
    print("-- DISPLAYING STORES --")
    for store in stores:
        print("Store ID: {}".format(store[0]))
        print("Address: {}".format(store[1])+"\n")

    main_menu_check()
#-----show_wishlist() method-----
def show_wishlist(cursor, userid):

    #Try to find wishlist_id's available to user_id
    cursor.execute("SELECT book.book_id, book_name, author, details FROM wishlist INNER JOIN book ON wishlist.book_id = book.book_id WHERE user_id = %s", (userid,))
    result = cursor.fetchall()

    #DISPLAY WISHLISTS
    if result:
        termclear()
        print("-- WISHLIST --")
        #Display books in WISHLIST ID
        for wishlist in result:
                print("Book ID: {}".format(wishlist[0]))
                print("Title: {}".format(wishlist[1]))
                print("Author: {}".format(wishlist[2]))
                print("Details: {}\n".format(wishlist[3]))

    account_menu_check(cursor, userid)
#-----show_books_to_add() method-----
def show_books_to_add(cursor, userid):

    cursor.execute("SELECT book.book_id, book_name, author, details FROM book WHERE NOT EXISTS(SELECT book_id FROM wishlist WHERE user_id = %s AND book.book_id = wishlist.book_id)", (userid,))
    
    addablebooks = cursor.fetchall()

    print("-- DISPLAYING ADDABLE BOOKS --")
    for book in addablebooks:
        print("Book ID: {}".format(book[0]))
        print("Book Name: {}".format(book[1]))
        print("Author: {}".format(book[2]))
        print("Details: {}".format(book[3]) + "\n")

    check_book_add(cursor, userid, addablebooks)

#Validation Methods
#-----validate_user() method-----   
def validate_user(cursor):
    userinput = input("Enter User ID: ")
    userinput = int(userinput)

    #Try to SELECT user using user_id
    cursor.execute("SELECT user_id FROM user WHERE user_id = %s", (userinput,))
    result = cursor.fetchone()

    #user_id found
    if result:
        termclear()
        userid = userinput
        show_account_menu(cursor, userid)

    #user_id not found
    else:
        termclear()
        print("INVALID USER TRY AGAIN!\n")
        validate_user(cursor)
#-----check_book_add() method-----
def check_book_add(cursor, userid, addablebooks):
    try:
        bookid = input("Please enter Book_ID to add: ")
        bookid = int(bookid)
    except ValueError:
        print("Invalid input. Please enter a valid numeric Book_ID.\n")

    bookfound = False

    #Run through list of available books if not available regect addition and print error
    for book in addablebooks:
        if bookid == book[0]:
            bookfound = True
            break

    if bookfound == True:
        termclear()
        add_books_to_wishlist(cursor, userid, bookid)
    else:
        termclear()
        print("Book not found. Please enter a valid Book_ID.\n")
        show_books_to_add(cursor, userid)

#Update methods
#-----add_books_to_wishlist() method-----
def add_books_to_wishlist(cursor, userid, bookid):
    #Ensure variables are proper form
    userid = int(userid)
    bookid = int(bookid)

    #Insert Book into Wishlist
    cursor.execute("INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)", (userid, bookid,))
    db.commit()

    cursor.execute("SELECT book_name FROM book WHERE book_id = %s", (bookid,))
    bookname = cursor.fetchone()

    bookname = str(bookname[0])

    #GET first_name and last_name FROM user
    cursor.execute("SELECT first_name, last_name FROM user WHERE user_id = %s", (userid,))
    username = cursor.fetchone()

    username = str(username[0])

    print("Added " + bookname + " into " + username + "'s Wishlist!")

    account_menu_check(cursor, userid)

#-----Database Connection Section------
#Database Config Section
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
#Attempts to connect using config then displays connection result
try:
    db = mysql.connector.connect(**config)
    
    #Prints Connection Info
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
#Tests for potential errors in connection to database
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
        print("The supplied username or password are invalid")
              
    elif err.errno == errorcode. ER_BAD_DB_ERROR: 
        print("The specified database does not exist")

    else:
        print(err)

#-----Code Start Section-----
finally: 
    cursor = db.cursor()

    #Code Start
    show_menu()
