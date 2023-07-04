from dbhelper import DBHelper
import sys


def do_input():
    id = int(input("Enter UserID : \t"))
    name = input("Enter User Name : \t")
    phone = input("Enter Phone Number : \t")
    db.insert_user(id, name, phone)

def do_fetch():
    db.fetch_all()

def do_delete():
    id = int(input("Enter UserID to be deletd :\t"))
    db.delete_user(id)

def do_update():
    id  = int(input("Enter UserID to be updated :\t"))
    name = input("Enter new Name :\t")
    phone = input("Enter new Phone number :\t")
    db.update_data(id, name, phone)


choice_dict = {
    1 : do_input,
    2 : do_fetch,
    3 : do_delete,
    4 : do_update,
    5 : sys.exit,
}

def main():
    global db 
    db = DBHelper()
    global choice
    while True:
        print("\n This will be an interactive concole \n")
        print("choose from below options : \n")
        print("ENTER 1 to insert data into table : ")
        print("ENTER 2 to fetch data from table : ")
        print("ENTER 3 to delete data from table : ")
        print("ENTER 4 to update data in table : ")
        print("ENTER 5 to exit program \n")
        choice = int(input())
        choice_dict.get(choice, lambda : print("Not a valid choice try again"))()


if __name__ == '__main__':
    main()