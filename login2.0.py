file_staff = "staff.txt"
file_customer= "customer.txt"
attempt = 3
def main_menu():
    global attempt #avoid run again attempt number will change to 3
    while True:
        print("[1] Registration\n[2] Login")
        try:
            option = int(input("Enter your choice:"))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 1:
            x = int(input("Are you staff or customer?\n[1]Staff\n[2]Customer\nEnter your choice:"))
            if x == 1:
                register_user(file_staff)
            elif x == 2:
                register_user(file_customer)

        elif option == 2:
            x = int(input("Are you staff or customer?\n[1]Staff\n[2]Customer\nEnter your choice:"))
            if x == 1:
                login_user(file_staff)
            elif x == 2:
                login_user(file_customer)
        else:
            print("Invalid choice. Please choose 1 or 2.")

def register_user(file_name):
    while True:
        username = input("Enter a username to register: ")
        password = input("Enter a password: ")

        if username and password:  # Ensure username and password are not empty
            with open(file_name, "a") as f:  # Always write to the same file
                f.write(f"{username},{password}\n")
                print("Registeration sucessful!")
                break
        else:
            print("Username or password cannot be empty.")

def login_user(filename):
    global attempt
    while attempt > 0:
        username = input("Enter a username to login: ")
        password = input("Enter a password: ")
        found = False
        try:
            with open(filename, "r") as f:
                lines = f.readlines()  # Read all lines in the file
        except FileNotFoundError:
            print("File not found. Please register first.")
            return
    
        for line in lines:
            line = line.strip().split(",")  # Strip newline and split by comma
        #去除行尾的换行符并按逗号分隔
        #strip去除头尾指定字符，默认为空格或者换行
        #split把“hi jiayi”变成“hi”，“jiayi”
            if len(line) == 2:  # Ensure the line has two parts (username, password)
                file_username, file_password = line
                if file_username == username and file_password == password:
                    print("Login successful!")
                    found = True
        if found:
            break            
        attempt -= 1
        if attempt > 0:
            print(f"Invalid username or password. You have {attempt} more attempts.")
        else:
            print("Login unsuccessful. No attempts left.")


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

main_menu()