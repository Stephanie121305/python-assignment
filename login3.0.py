file_staff = "staff.txt"
file_customer = "customer.txt"
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
            x = int(input("Are you staff or customer?\n[1]Staff\n[2]Customer\nEnter your choice:"))
            if x == 1:
                register_user(file_staff, attempts, staff = True)
            elif x == 2:
                register_user(file_customer, attempts, staff = False)
        elif option == 2:
            x = int(input("Are you staff or customer?\n[1]Staff\n[2]Customer\nEnter your choice:"))
            if x == 1:
                if login_user(file_staff, attempts):
                    break
            elif x == 2:
                if login_user(file_customer, attempts):
                    break
        else:
            print("Invalid choice. Please choose 1 or 2.")

def register_user(file_name, attempts, staff = False):
    while True:
        username = input("Enter a username to register: ")
        password = input("Enter a password: ")

        if username and password:
            if staff:  # Check if the user is staff
                role = input("Enter staff role (Admin/Manager/Chef): ")
                if role not in ['Manager', 'Chef']:
                    print("Invalid role. Please enter 'Manager' or 'Chef'.")
                    continue
                with open(file_name, "a") as f:
                    f.write(f"{username},{password},{role},{attempts}\n")
                    print(f"Registration successful! Registered as {role}.")
                    break
            else:
                with open(file_name, "a") as f:
                    f.write(f"{username},{password},{attempts}\n")
                    print("Registration successful!")
                    break
        else:
            print("Username or password cannot be empty.")
        
def login_user(filename, attempts):
    username = input("Enter a username to login: ")
    password = input("Enter a password: ")
    user_found = False
    updated_lines = [] 

    # Read file content
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found. Please register first.")
        return False

    for line in lines:
        line_data = line.strip().split(",")

        if len(line_data) == 3:  # Customer
            file_username, file_password, file_attempts = line_data[0], line_data[1], int(line_data[-1])
            role = "Customer"  # Customers don't have a specific role
        elif len(line_data) == 4:  # Staff
            file_username, file_password, role, file_attempts = line_data[0], line_data[1], line_data[2], int(line_data[-1])

        if file_username == username:
            user_found = True
            if file_attempts == 0:
                print("Login unsuccessful. No attempts left.")
                return False
            elif file_password == password:
                print("Login successful!")
                file_attempts = attempts  # Reset attempts after successful login
                role_menu(role)
                return True
            else:
                file_attempts -= 1
                print(f"Invalid password. You have {file_attempts} attempts remaining.")

        # Append the updated user information to the list
        updated_lines.append(f"{file_username},{file_password},{file_attempts}\n")

    # Update the file with new attempt counts
    with open(filename, "w") as f:
        f.writelines(updated_lines)

    if not user_found:
        print("Username not found. Please register.")
        return False

def check_user_exists(filename, username):
    """Check if the username already exists in the file."""
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        return False  # If file doesn't exist, user doesn't exist
    
    for line in lines:
        stored_username, _ = line.strip().split(",")
        if stored_username == username:
            return True
    return False

def role_menu(role):
    if role == "Admin":
        print("Welcome, Admin! You can perform the following actions:")
        print("[1] View Reports\n[2] Manage Staff\n[3] Approve Orders")
        option = input("Enter your choice: ")
        if option == "1":
            pass  # Function to handle viewing reports
        elif option == "2":
            pass# Function to manage staff
        elif option == "3":
            return  # Function to approve orders
        else:
            print("Invalid option. Please choose again.")
    
    elif role == "Manager":
        print("Welcome, Manager! You can perform the following actions:")
        print("[1] View Reports\n[2] Manage Staff\n[3] Approve Orders")
        option = input("Enter your choice: ")
        if option == "1":
            pass  # Function to handle viewing reports
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
            pass# Function to view the menu
        elif option == "2":
            pass  # Function to place an order
        elif option == "3":
            return  # Function to check order status
        else:
            print("Invalid option. Please choose again.")

    else:
        print("Unknown role. Please contact support.")

main_menu()

# login successful之后还一直跳login/register
#login failed不要show main menu
# login失败的时候textfile里面的role（Manager/Chef）会不见，我要保留这个role，login失败了之后manager会变成customer