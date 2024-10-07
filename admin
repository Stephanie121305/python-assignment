file_staff = "staff.txt"  #for login
file_manager = "manager.txt"
file_chef = "chef.txt"
file_admin = "admin.txt" #update own profile for admin
file_feedback = "feedback.txt"
def main_menu_admin():
    print("Choose option: \n-------------- \n1.Manage staff \n2.View sales report \n3.View feedback send by customer \n4.Update own profile")
    option = int(input("Please enter option:"))
    if 1 <= option <= 4:
        if option == 1:
            print("\nManage staff \n------------ \n1.Manager \n2.Chef")
            manage = int(input("Please enter option:"))
            if manage == 1:
                print("\nManager \n--------- \n1.Add \n2.Edit \n3.Delete")
                x = int(input("Please enter option:"))
                if x == 1:
                    add_staff(file_manager, file_staff)
                elif x == 2:
                    edit_staff(file_manager)
                elif x == 3:
                    delete_staff(file_manager, file_staff)
            else:
                print("\nChef \n--------- \n1.Add \n2.Edit \n3.Delete")
                y = int(input("Enter your option:"))
                if y == 1:
                    add_staff(file_chef, file_staff)
                elif y == 2:
                    edit_staff(file_chef)
                elif y == 3:
                    delete_staff(file_chef, file_staff)
        elif option == 2:
            print("Sales Report")
        elif option == 3:
            print("Feedback sent by customer \n---------------------")
            feedback(file_feedback)
        elif option == 4:
            print("Update own profile:")
            update_admin(file_admin)

    else:
        print("Please enter valid integer, (example: 1 to 4)")

def add_staff(fileworker, file_staff):
    print("\nAdding staff \n------------")
    staffID = input("Enter staffID: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    role = input("Enter role: ")

    with open(fileworker, "r") as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(",")
            if data[0] == staffID and data[1] == username and data[2] == password:
                print(f"{staffID}, {username}, {password} already exist.")


    with open(file_staff, "r") as f:
        lines = f.readlines()
        for line in lines:
            data = line.strip().split(",")
            if data[0] == username and data[1] == password:
                print(f"{username}, {password} already exist.")
                main_menu_admin()

    with open(fileworker, "a") as f:
        # write staffs' info to the file
        f.write(f"{staffID},{username},{password},{role}\n")

    with open(file_staff, "a") as f:
        f.write(f"{username},{password}\n")

    print(f"Hi, {username} with staffID:{staffID} added successfully.")
    main_menu_admin()

def edit_staff(fileworker):
    staffID = input(f"Enter staffID of the staff that you want to edit: ")
    username = input("Enter username of the staff that you want to edit: ")
    try:
        with open(fileworker, "r") as f:
            worker_lines = f.readlines() #read each line in the file into the lines list
    except FileNotFoundError:
        print(f"No staff records found")
        return

    try:
        with open(file_staff, "r") as f:
            staff_lines = f.readlines() #read each line in the file into the lines list
    except FileNotFoundError:
        print(f"No staff records found")
        return

    updated_worker = False
    new_worker_lines = []
    new_staff_lines = []

        for line in worker_lines:
            data = line.strip().split(",") #split the line with "," and spacing
            if data[0] == staffID: #data[0] represent the first data in the list (staffID)
                while True:
                    try:
                        print(f"Editing details for {username} with staffID:{staffID} \n1.StaffID \n2.Username \n3.Password \n4.Role \n5.Exit")
                        choice = int(input(f"Enter your choice on which you wish to edit: "))
                        if choice == 1:
                            data[0] = input(f"Enter new staffID: ")
                        elif choice == 2:
                            data[1] = input(f"Enter new username: ")
                        elif choice == 3:
                            data[2] = input(f"Enter new password: ")
                        elif choice == 4:
                            data[3] = input("Enter new role:")
                        elif choice == 5:
                            print("Exiting edit mode")
                            break
                        else:
                            print("Invalid input, please enter number 1 to 5")
                        updated_worker = True
                        print(f"{username}'s information updated successfully.")
                    except ValueError:
                        print("Invalid input. Please enter number.")
                new_worker_lines.append(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}")
                new_staff_lines.append(f"{data[1]},{data[2]}")
            else:
                new_worker_lines.append(line) #write back unmodified lines
        with open(fileworker, "w") as f:
            f.writelines(new_worker_lines)
        with open(file_staff,"w") as f:
            f.writelines(new_staff_lines)

    main_menu_admin()

def delete_staff(fileworker, file_staff):
    staffID = input("Enter staffID that you want to delete:")
    username = input("Enter username that you want to delete:")

    try:
        with open(fileworker, "r") as f:
            staff_lines = f.readlines()
    except FileNotFoundError:
        print("No staff records found.")
        return

    try:
        with open(file_staff, "r") as f:
            worker_lines = f.readlines()
    except FileNotFoundError:
        print("No staff records found.")
        return

    deleted_staff = False
    with open(fileworker, "w") as f:
        for line in staff_lines:
            data = line.strip().split(",")
            if data[0] == staffID:
                deleted_staff = True
                print(f"{staffID} has been delete successfully from record.")
            else:
                f.write(line) #write back unmodified lines
                print(f"No staff found with staffID: {staffID}")

    deleted_worker = False
    with open(file_staff, "w") as f:
        for line in worker_lines:
            data = line.strip().split(",")
            if data[0] == username:
                deleted_worker = True
                print(f"{username} has been delete successfully from record.")
            else:
                f.write(line) #write back unmodified lines
                print(f"No staff found with username: {username}")
    main_menu_admin()

def feedback(file_feedback):
    with open(file_feedback, "r")as f:
        lines = f.readlines()

        for line in lines:
            data = line.strip().split(',')
            customerID = data[0]
            rate = data[1]
            review = data[2]
            print(f"Customer:{customerID} gives rating of {rate} with review:{review}")

def update_admin(file_admin):
    with open(file_admin, "r") as f:
        lines = f.readlines()

    with open(file_admin, "w") as f:
        for line in lines:
            data = line.strip().split(",")
            print("\n1.Username \n2.Password \n3.Name \n4.Email \n5.Phone number \n6.Gender \n7.Years of experience \n8.Exit")
            pick = int(input("Enter your option:"))
            try:
                if pick == 1:
                    data[0] = input("Enter your new username:")
                    f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}\n")
                elif pick == 2:
                    data[1] = input("Enter your new password:")
                    f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}\n")
                elif pick == 3:
                    data[2] = input("Enter your new name:")
                    f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}\n")
                elif pick == 4:
                    data[3] = input("Enter your new email:")
                    f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}\n")
                elif pick == 5:
                    data[4] = input("Enter your new phone number:")
                    f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}\n")
                elif pick == 6:
                    data[5] = input("Enter your new gender:")
                    f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}\n")
                elif pick == 7:
                    data[6] = input("Enter your new years of experience:")
                    f.write(f"{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]}, {data[6]}\n")
                elif pick == 8:
                    print("Exiting update own profile.")
                    break
            except ValueError:
                print("Invalid input. Please enter number 1 to 8.")
        main_menu_admin()


main_menu_admin()

