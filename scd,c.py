import sys
import time
import client

print("\n【Server Code Desktop, Center】【SCD,C】【1.1v】")
print("【Offline State】\n")
while True:
    psw = input("Password[open code] >>>")
    if psw == "server":
        print("Correct Password")
        break
    else:
        print("Password Error\n")
        continue
while True:
    code = input("\nCode >>>")
    try:
        if code == "help":
            print("back: exit this window")
            print("save: save the data")
            print("exit: save and break the server")
            print("exit*: forced closing the server and exit this window")
            print("get information: get normal users information")
            print("get information*: get inside users information")
            print("new user: make a new user[computer, normal]")
            print("new user*: make a new user[computer, inside]")
        elif code == "back":
            sys.exit()
        elif code == "save":
            client.client_code_poster("save")
        elif code == "new user":
            username = input("Username >>>")
            password = input("Password >>>")
            client.client_normal_user(username, password)
        elif code == "new user*":
            username = input("Username >>>")
            password = input("Password >>>")
            usercode = input("Usercode >>>")
            client.client_inside_user(username, password, usercode)
        elif code == "exit":
            client.client_code_poster("exit")
            sys.exit()
        elif code == "exit*":
            code = input("Enter code[10025] >>>")
            if code == "10025":
                client.client_code_poster("exit*")
                sys.exit()
            else:
                print("Code Error")
                continue
        elif code == "get information":
            client.client_code_poster("get information")
        elif code == "get information*":
            client.client_code_poster("get information*")
        else:
            print(f"Code no found -> '{code}' ")
    except ConnectionRefusedError:
        print("服务器可能未开启 或 服务器过于繁忙")
        print("正在退出……")
        time.sleep(1)
        sys.exit()
