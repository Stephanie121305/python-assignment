print("Welcome to Pahpai Restauramt! Please choose the following catagories, if you like to quit the menu please press 0")
def MenuCatagories():
    print("[1] Rice")
    print("[2] Noodles")
    print("[3] Croissant")
    print("[4] Sides")
    print("[5] Beverages")

Option1 = {"Black Paper Chicken Chop Rice": 25.00,
           "Mushroom Chicken Chop Rice": 20.00,
           "Lemon Chicken Chop Rice": 21.00,
            "Salted Egg Chicken Chop Rice": 23.00}

Option2 =  {"Chicken Bolognaise Spagetti": 22.00,
           "Carbonara Spagetti": 20.00,
           "Aglio Olio Signature": 20.00,
            "Assam Pedas Spagettic": 22.00,
            "Mac & Cheese": 25.00}

Option3 = {"Chocolate Crossiant": 15.00,
           "Almond Crossiant": 15.00,
           "LNutella Crossiant": 15.00,
            "Veggie Cheese Crossiant": 18.00}

Option4 = {"French Fries": 10.00,
           "Onion Rings": 12.00,
           "Curly Fries": 12.00,
           "Chicken Wings": 20.00}

Option5 = {"Coke": 5.00,
           "100 Plus": 5.00,
           "Green Tea": 4.00,
           "Sprite": 4.00}

MenuCatagories()
option = int(input("Enter your option:"))

while option != 0:
    if option == 1:
        print("--------MENU--------")
        for key, value in Option1.items():
            print(f"{key:30}: RM{value:.2f}")
        print("-------------------")

    elif option == 2:
        print("--------MENU--------")
        for key, value in Option2.items():
            print(f"{key:30}: RM{value:.2f}")
        print("-------------------")

    elif option == 3:
        print("--------MENU--------")
        for key, value in Option3.items():
            print(f"{key:30}: RM{value:.2f}")
        print("-------------------")

    elif option == 4:
        print("--------MENU--------")
        for key, value in Option4.items():
            print(f"{key:20}: RM{value:.2f}")
        print("-------------------")
        
    elif option == 5:
        print("--------MENU--------")
        for key, value in Option5.items():
            print(f"{key:20}: RM{value:.2f}")
        print("-------------------")
    else:
        print("Invalid option")
    
    print()
    MenuCatagories()
    option = int(input("Enter your option:"))

print("Thank you for visiting Pahpai Restaurant!")


