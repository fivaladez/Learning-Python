import os, sys

clear = lambda: os.system('cls')

fp_path = os.getcwd() + os.sep + "Principal_Agenda.py"
ft_path = os.getcwd() + os.sep + "Temporary_Agenda.py"



personDict = {}
# name:[info, ..., info]

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
            pass
        else:
            print option, " is not a valid option"

def menu():
    clear()
    print "\n\n     ===== MENU ====="
    print "\n    1. Add a contact"
    print "\n    2. Look for a contact"
    print "\n    3. Eliminate a contact"
    print "\n    4. Erase agenda"
    print "\n    5. Exit"

    option_menu = input("\n\n    Introduce the option you want to execute: ")

    return option_menu

def add_contact():
    name_to_add = ""
    infoList = [""] * 2 #Initialize a list for 2 spaces
    clear()
    print "\n\n    ===== ADD CONTACT ====="
    name_to_add = raw_input("\n\n    Introduce the complete name to add: ")

    infoList[0] = raw_input("\n    Introduce the cellphone add: ")
    infoList[1] = raw_input("\n    Introduce the e-mail to add: ")

    personDict[name_to_add] = infoList

    print "\n    You intruduced: " + name_to_add +  ": ", personDict[name_to_add]

    with open( fp_path, "a") as fp:
        fp.write( name_to_add )
        fp.write( "\t" )
        fp.write( infoList[0] )
        fp.write( "\t" )
        fp.write( infoList[1] )
        fp.write( "\n\n" )

    raw_input("\n\n    Press<enter> to exit")

def look_for_contact():
    name_to_look_for = ""
    clear()
    print "\n\n    ===== LOOK FOR CONTACT ====="
    name_to_look_for = raw_input("\n\n    Introduce the complete name to look for: ")

    with open( fp_path, "r") as fp:
        agenda_file = fp.read()

    if name_to_look_for in agenda_file:
        location = agenda_file.find( name_to_look_for )
        print "\n    " + agenda_file[ location: location + 40]
    else:
        print "\n    That contact doesn't exist!"

    raw_input("\n\n    Press<enter> to exit")

def eliminate_contact():
    clear()
    print "\n\n    ===== ELIMINATE CONTACT ====="
    name_to_eliminate = raw_input("\n\n    Introduce the complete name to eliminate: ")

def erase_agenda():
    clear()
    print "\n\n    ===== ERASE AGENDA ====="


if __name__ == '__main__':
    main()
