import os

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
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        else:
            pass

def menu(self):
    print "    \n\n ===== MENU ====="
    print "    \n1. Add a contact"
    print "    \n2. Look for a contact"
    print "    \n3. Eliminate a contact"
    print "    \n4. Erase agenda"
    print "    \n5. Exit"

    option_menu = input("    \n\nIntroduce the option you want to execute: ")

    return option_menu

def add_contact(self):
    pass

def look_for_contact(self):
    pass

def eliminate_contact(self):
    pass

def erase_agenda(self):
    pass


if __name__ == '__main__':
    main()
