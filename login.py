file_staff = "staff.txt"
file_customer= "customer.txt"

attempt = 3
print("[1] Registration\n[2] Login")
option = int(input("Enter your choice:"))

if option == 1:  # Registration option
    x = int(input("Are you staff or customer?\n[1]Staff\n[2]Customer\nEnter your choice:"))
    if x == 1:
        def register_user():
            username = input("Enter a username to register: ")
            password = input("Enter a password: ")

            if username and password:  # Ensure username and password are not empty
                with open(file_staff, "a") as f:  # Always write to the same file
                    f.write(f"{username},{password}\n")
                    f.flush()
                print("Registeration sucessful!")

    
    register_user()  # Call the function to register a new user

elif option == 2:  # Login option
    while attempt > 0:
        username = input("Please enter your name: ") 
        password = input("Please enter your password: ")
        found = False
      
        with open("staff.txt", "r") as f:
            lines = f.readlines()  # Read all lines in the file

        for line in lines:
            line = line.strip().split(",")  # Strip newline and split by comma
        #去除行尾的换行符并按逗号分隔
        #strip去除头尾指定字符，默认为空格或者换行
        #split把“hi jiayi”变成“hi”，“jiayi”
        print("Hello World")
            if len(line) == 2:  # Ensure the line has two parts (username, password)
                file_username, file_password = line
                if file_username == username and file_password == password:
                    found = True
                    if username == "jiayi":
                        print("Welcome back! Manager")
                    elif username == "wanlin":
                        print("Welcome back! Administrator")
                    elif username == "iris":
                        print("Welcome back! Chef")
                    else:
                        print("Welcome back!")
                    break

        if found:
            break  # Exit the while loop if the user is found
        else:
            attempt -= 1
            if attempt > 0:
                print("Invalid username or password. You have", attempt, "more attempts.")
            else:
                print("Login unsuccessful.")
else:
    print("Invalid option. Please choose either 1 or 2.")
#要确保register过的不会再重复度欧一次，如果register过就要return already exist
#back如果option选错不用重新run
