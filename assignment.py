file_menu = "menu.txt"

def load_menu_from_text_file(file_name):
    menu = {}
    current_category = None

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("-"):
                current_category = line
                menu[current_category] = []
            elif line.startswith ("-"):
                submenu = line[2:] #start from index 2 until last
                menu[current_category].append(submenu)
    
    return menu

def add_menu(menu, category, submenu):
    if category in menu:
        if submenu:
            if submenu not in menu[category]:
                menu[category].append(submenu)
                print(f"Item '{submenu}' added to category '{category}'.")
            else:
                print(f"Item '{submenu}' already exists in category '{category}'.")
        else:
            print("Item name cannot be empty.")
    else:
        menu[category] = [submenu]
        print(f"Category '{category}' created and item '{submenu}' added.")

def edit_menu(menu, category, submenu):
    if category in menu:
        if old_submenu in menu:




def save_file(file_name, menu):
    with open(file_name, 'w') as f:
        for category, items in menu.items():
            f.write(category + '\n')
            for item in items:
                f.write(f"- {item}\n")

def main():
    menu = load_menu_from_text_file(file_menu)
    while True:
        print("Menu Management System\n[1]Add Menu\n[2]Edit Menu\n[3]Delete Menu")
        option = input("Enter your choice")
        if option == 1:
            category = input("Enter the category name:")
            if category in menu:
                submenu = input("Enter the submenu to add to category:")
                add_menu(menu, category, submenu)

        if option == 2:
            category = input("Enter the category name to edit:")
            old_submenu = input("ENter the submenu you want to edit:")
            new_submenu = input("Enter the new menu name:")
            edit_menu(menu, category, submenu)

        if option == 3:

