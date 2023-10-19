'''
LIST-PROGRAM.PY: Program for working with lists / dictionaries

__author__  = "Daniil Gurski"
__version__ = "3.11.4"
__email__   = "daniil.gurski@elev.ga.ntig.se"
'''

import os   # Used to clear the screen.
import re   # Regular expression for finding patterns inside user inputs. 
import json # Used to save program result. 
import colorama # Text colors

from colorama import Fore, Back
colorama.init(autoreset = True) # Adding color to one text will not affect next text lines.


def welcome_message(): 
    os.system("cls")

    # I used a single-line print because it's easier to read in this case. 
    print(f"{Back.BLUE}Welcome to the list program !")

    print(f"{Fore.CYAN}\nCATEGORIES:")
    print("Select category: category name")
    print("Create category: +category name")
    print("Remove category: -category name")

    print(f"{Fore.CYAN}\nMANAGE SELECTED CATEGORY: ")
    print("Add element = new name")
    print("Remove element = same name")
    print("Change element = choose a position in a list.")

    print(f"\nFinally, use enter to {Fore.CYAN}show your cateogies{Fore.RESET}, enter again to {Fore.RED}exit")
    print("_" * 40)


def get_list_range(list):      # Used to show available positions for changing list elements.
    return f"1-{len(list)}" if len(list) > 1 else len(list)


def show_as_list(list):
    if not len(list):
        print(f"{Fore.LIGHTBLACK_EX}Currently empty.")

    for index, item in enumerate(list):
        print(f"{index + 1}.) {item}")


# MAIN
loop_state = True

categories = {"my things" : []}
selected_category = list(categories)[0] # Selection of the default category at program startup

welcome_message()
while loop_state: 
    
    selected_list = categories[selected_category]
    
    print(f"\nList of category {Fore.LIGHTCYAN_EX}'{selected_category}'{Fore.RESET}: ")
    show_as_list(selected_list)

    user_input = input(f"ADD/REMOVE/CHANGE({get_list_range(selected_list)}):")

    # View existing categories / exit
    if user_input == "":
        os.system("cls")
        print(f"\nYour categories: ")
        show_as_list(categories.keys())

        user_input = input(f"{Fore.YELLOW}USE ENTER TO EXIT, ENTER THE CATEGORY NAME TO SWITCH: ")

        if user_input == "":
            loop_state = False
        
        selected_category = user_input if user_input in categories else selected_category


    # Switching to existing category.
    elif user_input in categories:
        selected_category = user_input


    # Creating category.
    elif re.search("^\+" , user_input):
        new_category = user_input[1:]   # eveything coming after '+'
        categories[new_category] = []

        selected_list = categories[new_category]
        selected_category = new_category

        os.system("cls")
        print(f"\nCategory {Fore.CYAN}'{new_category}'{Fore.RESET} has been successfully added.")
        continue


    # Removing category.
    elif re.search("^\-" , user_input):
        remove_target = user_input[1:]  # eveything coming after '-'

        if len(categories) > 1 and remove_target in categories:
            del categories[remove_target]
            selected_category = list(categories.keys())[-1]

            os.system("cls")
            print(f"Category {Fore.CYAN}'{remove_target}'{Fore.RESET} has been succesfully removed.")
            continue
        else:
            os.system("cls")
            print(f"\n{Fore.YELLOW}Make sure you have at least one category created or a category you entered exists.")
            continue


    # Changing elements by entering its position / index.
    elif user_input.isdigit():
        if int(user_input) > len(selected_list):
            os.system("cls")
            print(f"{Fore.YELLOW}No such item exists.")
            continue

        index = int(user_input) - 1 
        change_target = selected_list[index]

        user_input = input(f"Change {change_target} to: ")
        selected_list[index] = user_input


    # Removing element from the selected list
    elif user_input in selected_list:
        selected_list.remove(user_input)


    # Adding element from the selected list
    else:
        selected_list.append(user_input)
        
    os.system("cls")


print("\nYour created categories & lists:")
for category in categories:
    print(f"List of category {Fore.CYAN}'{category}'{Fore.RESET}: ")
    show_as_list(categories[category])
    

# Writing categories with the lists to the save.json file.
with open(r"C:\Users\daniil.gurski\Desktop\Prog.1\projekt-2\save.json", "w") as f:
    json.dump(categories, f)