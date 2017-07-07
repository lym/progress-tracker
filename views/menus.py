import os
import sys


""" Menu functions """


def main_menu():
    # Main menu
    os.system('clear')

    print("Welcome, Bootcamper\n\nWhat would you like to do today?")
    print("Please select a menu item:\n")
    print("1. View Skills")  # view_skills
    print("2. Add Skill")  # new_skill
    print("3. View accomplished skills")
    print("4. View skills to accomplish")
    print("5. View learning progress")
    print("\n0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)

    return


def view_skills():
    """ Skills index view """
    skills = [
        "Building Relationships",
        "Test Driven Development",
        "Agile Methodology",
        "Adaptability",
        "Asking Questions"
    ]
    print("Skills !\n")
    for skill in skills:
        print('* ' + skill + '\n')
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


# Menu 2
def new_skill():
    print("Add Skill\n")
    print("9. Back")
    print("0. Quit")
    choice = input(" >>  ")
    exec_menu(choice)
    return


def back():
    # Back to main menu
    menu_actions['main_menu']()


def exit():
    # Exit program
    sys.exit()
# from views.option_menu_mappings import menu_actions

# =======================
#    Option-to-menu mappings
# =======================


# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': view_skills,
    '2': new_skill,
    '9': back,
    '0': exit,
}


# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return
