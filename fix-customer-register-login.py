file_admin = "admin.txt"
file_manager = "manager.txt"
file_chef = "chef.txt"
file_customer = "customer.txt"
file_menu = "menu.txt"
file_order = "order.txt"
file_ingredient = "ingredient.txt"

def main_menu():
    while True:
        print("Are you customer or staff?\nIf you are customer please enter 1, staff enter 2.")
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
                login_attempts = 3
                if role == 1:
                    login(file_admin, login_attempts)
                elif role == 2:
                    login(file_manager, login_attempts)
                elif role == 4:
                    login(file_chef, login_attempts)
                
            else:
                print("Invalid choice. Please enter valid number.")
        else:
                print("Invalid choice. Please enter valid number.")

def register_user(file_customer):
    while True:
        print("Have you been register or not? \nIf yes please enter [1], if no please enter [2].")
        choice = int(input("Please enter your choice:"))
        if choice == 1:
            login(file_customer, False)
        elif choice == 2:
            username = input("Enter a username to register: ")
            password = input("Enter a password: ")
            name = input("Enter your name as IC:")
            email = input("Enter your email:")
            phone = input("Enter your phone number:")
            gender = input("Enter your gender(eg.Male/Female):")
            if username and password:
                id = ""
                with open(file_customer, "r") as f:
                    lines = f.readlines()
                    id = "C" + str(len(lines) + 1)
                with open(file_customer, "a") as f:
                    f.write(f"{id},{username},{password},{name},{email},{phone},{gender}\n")
                    f.flush()
                    print("Registration successful!")
                    role_menu("Customer")
                    break
            else:
                print("Username or password cannot be empty.")#after customer register register successful jump to customer function
        else:
            print("Invalid choice. Please enter 1 or 2.")
        
def login(user_file, login_attempts):
    username = input("Enter a username to login: ")
    password = input("Enter a password: ")
    user_found = False

    try:
        with open(user_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found. Please register first.")
        return False

    for line in lines:
        line_data = line.strip().split(",")

        file_username, file_password = line_data[1], line_data[2]

        if file_username == username:
            user_found = True
            if login_attempts != False:
                if login_attempts == 0:
                    print("Login unsuccessful. No attempts left.")
                    return False
                elif file_password == password:
                    print("Login successful!")
                    role_menu(line_data[3])
                    return True
                else:
                    login_attempts -= 1
                    print("Invalid password. You have {} attempts remaining.".format(login_attempts))
                    if login_attempts == 0:
                        print("No attempts left.")
                        return False
                    login(user_file, login_attempts)
            else: 
                if file_password == password:
                    print("Login successful!")
                    role_menu('Customer')
                    return True
                else: 
                    if line == lines[-1]:
                        login(user_file, login_attempts)
    if not user_found:
        print("Username not found.")
    return False

def role_menu(role):
    if role == "Admin":
        print("Welcome, Admin! You can perform the following actions:")

    
    elif role == "Manager":
        print("Welcome, Manager! You can perform the following actions:")
        print("[1] Manage Customer\n[2] Manage Menu\n[3] View ingredient\n[4] Update Own Profile\n[5] Log Out")
        option = int(input("Enter your choice:"))
        if option == 1:
            manager_menu()
        elif option == 2:
            pass
        elif option == 3:
            view_ingredient()
        elif option == 4:
            pass  # Function to approve orders
        elif option == 5:
            pass  # Function to approve orders
        
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
        print("[1] View Menu\n[2] Place Order\n[3] Check Order Status\n[4] Log Out")
        option = input("Enter your choice: ")
        if option == "1":
            pass
        elif option == "2":
            pass  # Function to place an order
        elif option == "3":
            pass  # Function to check order status
        elif option == "4":
            pass  # Function to check order status
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

def manager_menu():
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

    while True:
        print("[1] Delete Customer\n[2]Back")
        option = int(input("Enter your choice:"))

        if option == 1:
            delete_customer(file_customer)  
        elif option == 2:
            break

def view_ingredient():
    ingredient_dict = {}
    with open(file_ingredient,"r") as f:
                for line in f:
                    line = line.strip().split(",")
                    ingredient, quantity, price_per_unit, total_price = line[0], line[1], line[2], line[3]
                    ingredient_dict[ingredient] = {
                                            "Total quantity": int(quantity),
                                            "Total Price Per Unit": float(price_per_unit),
                                            "Total Price": float(total_price)
                                            }

    print(f"{'Ingredient':<15}{'Total Quantity':<15}{'Price Per Unit (RM)':<20}{'Total Price (RM)':<15}")
    print("-" * 70)

    for ingredient, amount in ingredient_dict.items():
        print(f"{ingredient:<15}{amount['Total quantity']:<15}{amount['Total Price Per Unit']:<20.2f}{amount['Total Price']:<16.2f}")

main_menu()


#order function add()quantity #customerid invoice id total price id of chef date(completed(payment.txt))
#order history import datetime, customer id, menu id, chef id, quantity, pay to comform = total price, profit based on month
#order
#sales report need to include what information:food id, food name, price, total price date(month)based on chef id to show sales report
#customer update own profile in register
#customer order many food have many orderid such as A01,A02,A03 based on invoice id to give chef
