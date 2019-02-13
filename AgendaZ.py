import os, sys

clear = lambda: os.system('cls')

fp = open( os.getcwd() + os.sep + "Principal_Agenda.py", "a+")
fp.close()
ft = open( os.getcwd() + os.sep + "Temporary_Agenda.py", "a+")
ft.close()


personDict = {}
# name:infoList[]

def main():
    """"""
    while True:
        option = menu()
        if option == 1:
            add_contact()
        elif option == 2:
            look_for_contact()
        elif option == 3:
            eliminate_contact()
        elif option == 4:
            erase_agenda()
        elif option == 5:
            sys.exit("Good bye ...")
        else:
            print option, " is not a valid option"

def menu():
    print "    \n\n ===== MENU ====="
    print "    \n1. Add a contact"
    print "    \n2. Look for a contact"
    print "    \n3. Eliminate a contact"
    print "    \n4. Erase agenda"
    print "    \n5. Exit"

    option_menu = input("    \n\nIntroduce the option you want to execute: ")

    return option_menu

def add_contact():
    clear()
    print "    \n\n===== ADD CONTACT ====="

def look_for_contact():
    clear()
    print "    \n\n===== LOOK FOR CONTACT ====="

def eliminate_contact():
    clear()
    print "    \n\n===== ELIMINATE CONTACT ====="

def erase_agenda():
    clear()
    print "    \n\n===== ERASE AGENDA ====="


if __name__ == '__main__':
    main()
