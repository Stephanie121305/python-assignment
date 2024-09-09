user1 = ["jiayi","1213"]
user2 = ["wanlin","1234"]
user3 = ["iris","1234"]
login_change = 3


while login_change>0:
    username = input("Please enter your name:") 
    password = input("Please enter your password:")

    if username == user1[0] and password == user1[1]:
        print("Welcome back Administrator")
        break
    if username == user2[0] and password == user2[1]:
        print("Welcome back Manager")
        break
    if username == user3[0] and password == user3[1]:
        print("Welcome back Chef")
        break
    
    else:
        login_change -= 1
        if login_change > 0:
            print("Username or password incorrect. You have ",login_change,"more change")
        else:
            print("Login unsuccessful")
            

