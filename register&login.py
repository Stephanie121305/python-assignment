from tkinter import * #用他的function前面可以不用加tk.

def register_user():
    username = namevalue.get()
    password = passwordvalue.get()
    
    if username and password:  # 确保用户名和密码都不为空
        with open("data.txt", "a") as f:  # 使用 "a" 模式打开文件进行追加写入
            f.write(f"{username},{password}\n")
        result_label.config(text="Registration successful!") #config():用于更改部件（如按钮、标签、输入框等）属性的一种通用方法，ex：
    else:
        result_label.config(text="Please fill in all fields.")

# 设置主窗口
root = Tk() #建立视窗
root.geometry('500x300')
root.title('Registration Form')

# 创建标签和输入框
Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=10) #padx=x轴
Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=10) #pady=y轴

namevalue = StringVar()
passwordvalue = StringVar()

nameentry = Entry(root, textvariable=namevalue) #Entry=input n ouput
passwordentry = Entry(root, textvariable=passwordvalue, show='*')

nameentry.grid(row=0, column=1, padx=10, pady=10)
passwordentry.grid(row=1, column=1, padx=10, pady=10)

# 创建注册按钮
register_button = Button(root, text="Register", command=register_user)
register_button.grid(row=2, column=1, pady=10)

# 显示结果的标签
result_label = Label(root, text="")
result_label.grid(row=3, column=1, pady=10)

# 运行主循环,没有这个root会自己关闭
root.mainloop()

attempt = 3

while attempt > 0:
    username = input("Please enter your name:") 
    password = input("Please enter your password:")
    found = False
      
    with open("data.txt", "r") as f:#r是read
        lines = f.readlines()#读每一行
    for line in lines:
        line = line.strip().split(",")  # 去除行尾的换行符并按逗号分隔
        #strip去除头尾指定字符，默认为空格或者换行
        #split把“hi jiayi”变成“hi”，“jiayi”
        if len(line) == 2:  # 确保行里有两个部分
            file_username, file_password = line
            if file_username == username and file_password == password:
                found = True
                if username == "jiayi":
                      print("Welcome back! Manager")
                     
                elif username == "Iris":
                      print("Welcome back! Administrator")
                      
                elif username == "ziyan":
                      print("Welcome back! Chef")
                   
    if found:
         break
    else:
        attempt -= 1
        if attempt > 0:
            print("Invalid username or password. You have",attempt,"more attempt")
        else:
            print("Login unsuccessful")
        