file_admin = "admin.txt"
file_manager = "manager.txt"
file_chef = "chef.txt"
file_customer = "customer.txt"
file_staff = "staff.txt"
file_login_attempts = "attempts.txt"
file_menu = "menu.txt"
attempts = 3

def main_menu():
    while True:
        print("[1] Registration\n[2] Login")
        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            register_user(file_customer)
        elif option == 2:
            role = int(input("Choose your role:\n[1]Admin\n[2]Manager\n[3]Chef\n\nEnter your choice:"))
            if role in range(1,4):
                login_staff(file_staff, attempts)
            else:
                print("Invalid choice. Please enter valid number.")
        else:
                print("Invalid choice. Please enter valid number.")

def register_user(file_customer):
    while True:
        username = input("Enter a username to register: ")
        password = input("Enter a password: ")

        if username and password:
            with open(file_customer, "a") as f:
                f.write(f"{username},{password}\n")
                print("Registration successful!")
                role_menu("Customer")
                break
        else:
            print("Username or password cannot be empty.")#after customer register register successful jump to customer function
        
def login_staff(file_staff, attempts):
    username = input("Enter a username to login: ")
    password = input("Enter a password: ")
    user_found = False
    login_attempts = check_attempts(username, file_login_attempts)

    # Read file content
    try:
        with open(file_staff, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found. Please register first.")
        return False

    for line in lines:
        line_data = line.strip().split(",")
        file_username, file_password = line_data[1], line_data[2]

        if file_username == username:
            user_found = True
            if login_attempts == 0:
                print("Login unsuccessful. No attempts left.")
                return False
            elif file_password == password:
                print("Login successful!")
                file_attempts = attempts  # Reset attempts after successful login
                reset_attempts(username, file_login_attempts)
                role_menu(line_data[3])
                return True
            else:
                update_attempts(username, "Incorrect password")
                print("Invalid password. You have {} attempts remaining.".format(login_attempts - 1))
                login_attempts -= 1
                if login_attempts == 0:
                    print("No attempts left.")
                return False
    if not user_found:
        print("Username not found.")
    return False
 
def check_attempts(username, file_login_attempts):
    try:
        with open(file_login_attempts,"r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return attempts
    for line in lines:
        file_username, file_attempts = line.strip().split(",")
        if file_username == username:
            return int(file_attempts)
    return attempts

def update_attempts(username, remaining_attempts, file_login_attempts):
    try:
        with open(file_login_attempts, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []
    
    updated_lines = []
    user_found = False

    for line in lines:
        file_username, _ = line.strip().split(",")
        if file_username == username:
            updated_lines.append(f"{username},{remaining_attempts}\n")
            user_found = True
        else:
            updated_lines.append(line)

    if not user_found:
        updated_lines.append(f"{username},{remaining_attempts}\n")

    with open(file_login_attempts, "w") as f:
        f.writelines(updated_lines)

def reset_attempts(username, remaining_attempts,file_login_attempts):
    """登录成功后，将 login.txt 中用户的尝试次数重置为初始值"""
    update_attempts(username, remaining_attempts, file_login_attempts)

def role_menu(role):
    if role == "Admin":
        
    
    elif role == "Manager":
        print("Welcome, Manager! You can perform the following actions:")
        print("[1] Manage Customer\n[2] Manage Menu\n[3] View ingredient\n[4] Update Own Profile")
        option = input("Enter your choice: ")
        if option == "1":
            file_customer = "customer.txt"
            def add_customer(file_customer):
                customer_username = input("Enter the customer name you want to add:")
                customer_password = input("Enter the customer password you want to add:")
                user_found = False
                with open(file_customer,"r") as f:
                    for line in f:
                        line = line.strip().split(",")
                        file_customer_username, file_customer_password = line[0], line[1]
                        if file_customer_username == customer_username and file_customer_password == customer_password:
                            print(customer_username,"and",customer_password,"is already exist")
                            user_found = True
                            break
                    if not user_found:
                        with open(file_customer, "a") as f:
                            f.write(f"{customer_username},{customer_password}\n")
                        print(f"Customer {customer_username} added successfully!")
            main_menu()

            def edit_customer(file_customer):
                old_customer_username = input("Enter the customer name you want to edit:")
                old_customer_password = input("Enter the customer password you want to edit:")
                user_found = False
                updated_lines = []
                with open(file_customer,"r") as f:
                    for line in f:
                        line = line.strip().split(",")
                        file_customer_username, file_customer_password = line[0], line[1]
                        if file_customer_username == old_customer_username and file_customer_password == old_customer_password:
                            print(f"Customer {file_customer_username} found!")
                            new_username = input("Enter the new customer username: ")
                            new_password = input("Enter the new customer password: ")
                            new_line = f"{new_username},{new_password}\n"
                            updated_lines.append(new_line)
                            user_found = True
                        else:
                            updated_lines.append(",".join(line) + "\n")#因为line.strip().split(",")把它分开了，这里的line是我原本的，没有要修改的再用join把他们合并起来
                        
                    if user_found:
                        with open(file_customer, "w") as f:
                            f.writelines(updated_lines)
                        print("Customer details updated successfully!")
                    else:
                        print("Customer not found.")
                main_menu()

            def delete_customer(file_customer):
                old_customer_username = input("Enter the customer name you want to delete:")
                old_customer_password = input("Enter the customer password you want to delete:")
                user_found = False
                update_lines = []
                with open(file_customer,"r") as f:
                    for line in f:
                        line = line.strip().split(",")
                        file_customer_username, file_customer_password = line[0], line[1]
                        if file_customer_username == old_customer_username and file_customer_password == old_customer_password:
                            print(f"Customer {file_customer_username} found and deleted.")
                            user_found = True
                        else:
                            # 将不匹配的行保留
                            update_lines.append(",".join(line) + "\n")
                    
                    if user_found:
                        with open(file_customer, "w") as f:
                            f.writelines(update_lines)
                        print("Customer deleted successfully!")
                    else:
                        print("Customer not found.")
                main_menu()

            def main_menu():
                print("[1] Add Customer\n[2] Edit Customer\n[3] Delete Customer")
                option = int(input("Enter your choice:"))

                if option == 1:
                    add_customer(file_customer)
                elif option == 2:
                    edit_customer(file_customer)
                elif option == 3:
                    delete_customer(file_customer)

            main_menu()
  
        elif option == "2":
            pass# Function to manage staff
        elif option == "3":
            return  # Function to approve orders
        else:
            print("Invalid option. Please choose again.")

    elif role == "Chef":
        print("Welcome, Chef! You can perform the following actions:")
        print("[1] View Today's Orders\n[2] Update Inventory\n[3] Mark Order as Completed")
        option = input("Enter your choice: ")
        if option == "1":
            pass# Function to view today's orders
        elif option == "2":
            pass  # Function to update inventory
        elif option == "3":
            return# Function to mark an order as completed
        else:
            print("Invalid option. Please choose again.")

    elif role == "Customer":
        print("Welcome, Customer! You can perform the following actions:")
        print("[1] View Menu\n[2] Place Order\n[3] Check Order Status")
        option = input("Enter your choice: ")
        if option == "1":
            with open(file_menu,"r") as f:# Function to view the menu
                for line in f:
                    line = line.strip()
                    print(line)

        elif option == "2":
            pass  # Function to place an order
        elif option == "3":
            return  # Function to check order status
        else:
            print("Invalid option. Please choose again.")

    else:
        print("Unknown role. Please contact support.")

def admin_menu():
    print("Welcome, Admin! You can perform the following actions:")
    print("[1] Manage Staff\n[2] View report\n[3] Approve Orders")
    option = input("Enter your choice: ")
    if option == "1":
        pass  # Function to handle viewing reports
    elif option == "2":
        pass# Function to manage staff
    elif option == "3":
        return  # Function to approve orders
    else:
        print("Invalid option. Please choose again.")
main_menu()


#order function add()quantity
#order history import datetime, customer id, menu id, chef id, quantity, pay to comform = total price, profit based on month
#order