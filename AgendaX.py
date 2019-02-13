import os, sys

clear = lambda: os.system('cls')

fp_path = os.getcwd() + os.sep + "Principal_Agenda.txt"
ft_path = os.getcwd() + os.sep + "Temporary_Agenda.txt"

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
    cellphone_number = ""
    e_mail = ""
    clear()
    print "\n\n    ===== ADD CONTACT ====="

    name_to_add      = raw_input("\n\n    Introduce the complete name to add: ")
    cellphone_number = raw_input("\n    Introduce the cellphone add: ")
    e_mail           = raw_input("\n    Introduce the e-mail to add: ")

    print "\n    You intruduced: " + name_to_add + "  " + cellphone_number + "  " + e_mail

    with open( fp_path, "a") as fp:
        fp.write( name_to_add )
        fp.write( "  " )
        fp.write( cellphone_number )
        fp.write( "  " )
        fp.write( e_mail )
        fp.write( "\n\n" )

    raw_input("\n\n    Press<enter> to exit")

def look_for_contact():
    name_to_look_for = ""
    line_found = 0
    clear()
    print "\n\n    ===== LOOK FOR A CONTACT ====="
    name_to_look_for = raw_input("\n\n    Introduce the complete name to look for: ")

    with open( fp_path, "r") as fp:
        agenda_file = fp.readlines()

        for line in agenda_file:
            if name_to_look_for in line:
                print "\n    ", line
                line_found = 1

        if 0 == line_found:
            print "\n    That contact doesn't exist!"

    raw_input("\n\n    Press<enter> to exit")

def eliminate_contact():
    name_to_eliminate = ""
    line_eliminated = 0
    clear()
    print "\n\n    ===== ELIMINATE A CONTACT ====="
    name_to_eliminate = raw_input("\n\n    Introduce the complete name to eliminate: ")

    with open( fp_path, "r") as fp:
        agenda_file = fp.readlines()#Return a list of the lines

        for line in agenda_file:
            if name_to_eliminate in line:
                print "\n    The information to eliminate is: ", line
                line_eliminated = 1
            else:
                with open( ft_path, "a") as ft:
                    ft.write( line )
                    print "    Writing line ...\n"

        if 0 == line_eliminated:
            print "\n    That contact doesn't exist!"

    os.remove( fp_path )
    os.rename( ft_path, fp_path )

    raw_input("\n\n    Press<enter> to exit")

def erase_agenda():
    clear()
    print "\n\n    ===== ERASE AGENDA ====="

    os.remove( fp_path )

    raw_input("\n\n    Press<enter> to exit")


if __name__ == '__main__':
    main()
