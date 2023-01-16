from BST import BST
import os

""" Simple BST analyzer program.

This program is a proof of concept for the BST class. It allows the user to insert values into the tree and then analyze it.

"""

program = True
tree = None
error = ""
content = ""

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def insert():
    global tree
    global error
    
    value = ""
    error = ""

    while value != "exit":
        clear()
        print("\t-- Insert --\n")

        display()

        print("Type 'exit' or use control-C to cancel")
        value = input("Value to insert : ")

        if value.isnumeric():
            value = int(value)

            if BST.search(tree, value) != False:
                error = "The node you are trying to insert is already in the tree. The tree risks to become unbalanced."
            else:
                tree = BST.smart_plant(tree, value)

        else:
            error = "Illegal input."
    error = ""

def delete():
    global tree
    global error

    value = ""

    while value != "exit":
        clear()
        print("\t-- Delete --\n")
        
        display()

        print("Type 'exit' or use control-C to cancel")
        value = input("Value to delete : ")

        if value.isnumeric():
            value = int(value)

            # TODO: implement a the smart delete function to automatically balance the tree
            temp = BST.delete_node(tree, value)

            if temp is None:
                error = "The node you are trying to delete is not in the tree."
            else:
                tree = temp
        else:
            error = "Illegal input."
    error = ""

def search():
    global tree
    global content
    global error

    clear()
    print("\t-- Search --\n")

    value = ""
    while value != "exit":
        clear()
        display()

        print("Type 'exit' or use control-C to cancel")
        value = input("Value to search : ")

        if value.isnumeric():
            value = int(value)
            temp = BST.search(tree, value)
            if temp != False:
                content = f"The node you are looking for is in the tree. It's value is {temp.value}."
            else:
                content = "The node you are trying to search is NOT in the tree."

        else:
            error = "Illegal input."

    error = ""
    
def import_default():
    global tree

    tab  = [21, 8, 9, 3, 15, 19, 20, 7, 2, 1, 5, 6, 4, 13, 14, 12, 17, 16, 18]
    tree = BST.create_balanced_bst(tab)

def display():
    global error
    global content

    tab = BST.levelorder(tree)

    print("Initial values : ", tab)
    print("Sorted values  : ", BST.sort(tab))


    print("Current tree: ", tree)
    print("Height : ", BST.height(tree))
    print("Size   : ", BST.size(tree))

    print("Min    : ", BST.minimum_node(tree))
    print("Max    : ", BST.maximum_node(tree))

    print()

    if error != "":
        print('\033[93m' + f"Warning: {error}" + '\033[0m' + '\n')
        error = ""

    if content != "":
        print('\033[94m' + f"Info: {content}" + '\033[0m' + '\n')
        content = ""

def menu():
    global tree
    global error
    global content

    print("\n\t-- BST Analyzer --\n")

    display()

    print("-" * 35,"\n")

    print("Select the number of the functionality you want to use:")

    for i, func in enumerate(functionality):
        print(f"\t{i+1}. {func['name']}")

    response = input(">>> ")

    if response.isnumeric():
        response = int(response)
        if response > 0 and response <= len(functionality):
            if functionality[response-1]["function"] is not None:
                try:
                    functionality[response-1]["function"]()
                except KeyboardInterrupt:
                    content = "returning to menu..."
            else:
                error = "Functionality not implemented yet."
        else:
            error = "Invalid option."

    else:
        error = "Illegal input."

# main program

functionality = [
    {
        "name": "Insert",
        "function": insert
    },
    {
        "name": "Delete",
        "function": delete
    },
    {
        "name": "Search",
        "function": search
    },
    {
        "name": "Import default values",
        "function": import_default
    },
    {
        "name": "Exit",
        "function": exit
    }
]

while program:
    clear()

    try :
        menu()
    except KeyboardInterrupt:
        program = False

    if program == False:
        print("\n\nGoodbye!\n")