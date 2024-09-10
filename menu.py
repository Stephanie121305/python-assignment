file_menu = "menu.txt"
# 我add了新的menu可是textfile里面没有show，可是output show already exist
def load_menu_from_text_file(file_name):
    menu = {}
    current_category = None

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("-"):
                current_category = line
                menu[current_category] = []
            elif line.startswith("-"):
                submenu = line[2:]  # Start from index 2 to skip the dash and space
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
            print("Submenu name cannot be empty.")
    else:
        menu[category] = [submenu]
        print(f"Category '{category}' created and item '{submenu}' added.")

def edit_menu(menu, category, old_submenu, new_submenu):
    if category in menu:
        if old_submenu in menu[category]:
            # Replace the old submenu with the new submenu
            index = menu[category].index(old_submenu)
            menu[category][index] = new_submenu
            print(f"Submenu '{old_submenu}' in category '{category}' changed to '{new_submenu}'.")
        else:
            print(f"Submenu '{old_submenu}' does not exist in category '{category}'.")
    else:
        print(f"Category '{category}' does not exist.")

def delete_menu(menu, category, submenu):
    if category in menu:
        if submenu in menu[category]:
            menu[category].remove(submenu)
            print(f"Submenu '{submenu}' deleted from category '{category}'.")
            if not menu[category]:  # If the category is empty after deletion, remove the category
                del menu[category]
                print(f"Category '{category}' is empty and has been deleted.")
        else:
            print(f"Submenu '{submenu}' does not exist in category '{category}'.")
    else:
        print(f"Category '{category}' does not exist.")

def save_file(file_name, menu):
    with open(file_name, 'w') as f:
        for category, items in menu.items():
            f.write(category + '\n')
            for item in items:
                f.write(f"- {item}\n")

def main():
    menu = load_menu_from_text_file(file_menu)
    
    while True:
        print("\nMenu Management System")
        print("[1] Add Menu")
        print("[2] Edit Menu")
        print("[3] Delete Menu")
        print("[0] Quit")
        
        option = input("Enter your choice: ")
        
        if option == '0':
            break
        
        elif option == '1':
            category = input("Enter the category name: ")
            submenu = input("Enter the submenu to add: ")
            add_menu(menu, category, submenu)
        
        elif option == '2':
            category = input("Enter the category name to edit: ")
            old_submenu = input("Enter the submenu you want to edit: ")
            new_submenu = input("Enter the new submenu name: ")
            edit_menu(menu, category, old_submenu, new_submenu)
        
        elif option == '3':
            category = input("Enter the category name to delete from: ")
            submenu = input("Enter the submenu to delete: ")
            delete_menu(menu, category, submenu)
        
        else:
            print("Invalid option. Please try again.")
    
    try:
        save_file(file_menu, menu)
    except Exception as e:
        print(f"An error occurred while saving: {e}")


if __name__ == "__main__":
    main()

'''def show_main_menu(menu):
    print("Main Menu")
    for index, category in enumerate(menu,start = 1):
        print(f'[{index}] {category}')
    print("[0] Quit")
    return list(menu.keys())'''

'''def show_submwnu(category, item):
    print(f'\n{category} Menu:')
    for index, item in enumerate(item,start = 1):
        print(f'[{index}] {item}')
    print("[0] Back to Main Menu")'''

'''def main():
    category = show_main_menu(menu)
    choice = input('Enter your choice (0 to quit)')'''