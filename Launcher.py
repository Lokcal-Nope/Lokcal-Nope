import random
import client
import tkinter as tk

main_root = tk.Tk()
main_root.title("Test Messagebox Title 待定标题")
width = 750
height = width * 2 // 3
screen_width = main_root.winfo_screenwidth()
screen_height = main_root.winfo_screenheight()
main_root.geometry(f"{width}x{height}")
alignstr = '%dx%d+%d+%d' % (width, height, (screen_width-width)/2, (screen_height-height)/2)
main_root.geometry(alignstr)

m_tip = random.randint(1, 12)
if m_tip == 1 or m_tip == 11:
    main_tip = tk.Label(main_root, text="こんにちは!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 2:
    main_tip = tk.Label(main_root, text="Welcome!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 3 or m_tip == 12:
    main_tip = tk.Label(main_root, text="欢迎!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 4:
    main_tip = tk.Label(main_root, text="Bienvenido!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 5:
    main_tip = tk.Label(main_root, text="Bem vindo!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 6:
    main_tip = tk.Label(main_root, text="Bienvenu!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 7:
    main_tip = tk.Label(main_root, text="Herzlich willkommen!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 8:
    main_tip = tk.Label(main_root, text="Здравствуйте!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 9:
    main_tip = tk.Label(main_root, text="안녕하세요!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)
elif m_tip == 10:
    main_tip = tk.Label(main_root, text="Salve!", background="light gray", font="黑体")
    main_tip.place(relx=0.20, rely=0.00)
    main_tip.place(relwidth=0.60, relheight=0.05)

main_button1 = tk.Button(main_root, text="11111")
main_button1.place(relx=0.05, rely=0.05)
main_button1.place(relwidth=0.30, relheight=0.45)

main_button2 = tk.Button(main_root, text="22222")
main_button2.place(relx=0.35, rely=0.05)
main_button2.place(relwidth=0.30, relheight=0.45)

main_button3 = tk.Button(main_root, text="33333")
main_button3.place(relx=0.65, rely=0.05)
main_button3.place(relwidth=0.30, relheight=0.45)

main_button4 = tk.Button(main_root, text="44444")
main_button4.place(relx=0.05, rely=0.50)
main_button4.place(relwidth=0.30, relheight=0.45)

main_button5 = tk.Button(main_root, text="55555")
main_button5.place(relx=0.35, rely=0.50)
main_button5.place(relwidth=0.30, relheight=0.45)


def a_setting():
    as_root = tk.Tk()
    as_root.title("更多设置")
    as_width = 300
    as_height = as_width*2//3
    as_screen_width = as_root.winfo_screenwidth()
    as_screen_height = as_root.winfo_screenheight()
    as_root.geometry(f"{as_width}x{as_height}")
    as_alignstr = '%dx%d+%d+%d' % (as_width, as_height, (as_screen_width - as_width)/2,
                                   (as_screen_height - as_height)/2)
    as_root.geometry(as_alignstr)

    def signup():
        su_root = tk.Tk()
        su_root.title("注册普通账号")
        su_width = 300
        su_height = su_width * 2 // 3
        su_screen_width = su_root.winfo_screenwidth()
        su_screen_height = su_root.winfo_screenheight()
        su_root.geometry(f"{su_width}x{su_height}")
        su_alignstr = '%dx%d+%d+%d' % (su_width, su_height, (su_screen_width - su_width)/2,
                                       (su_screen_height - su_height)/2)
        su_root.geometry(su_alignstr)

        # ---------------------------------------------------
        su_text = tk.Label(su_root, text="用户名：")
        su_text.place(anchor="w", rely=0.1)
        su_username_entry = tk.Entry(su_root, font=('微软雅黑', 20))
        su_username_entry.place(width=280, rely=0.2, relx=0.05)
        su_text_ = tk.Label(su_root, text="密码：")
        su_text_.place(anchor="w", rely=0.6)
        su_password_entry = tk.Entry(su_root, font=('微软雅黑', 20))
        su_password_entry.place(width=280, rely=0.5, relx=0.05)
        # ----------------------------------------------------

        def su_post():
            su_username = su_username_entry.get()
            su_password = su_password_entry.get()
            client.client_normal_user(su_username, su_password)
        su_get_button = tk.Button(su_root, text="提交", command=su_post)
        su_get_button.pack()
        su_root.mainloop()
    as_button_signup_n = tk.Button(as_root, text="注册普通账号", command=signup)
    as_button_signup_n.pack(fill='x')
    
    as_button_signup_m = tk.Button(as_root, text="注册成员账号")
    as_button_signup_m.pack(fill='x')
    
    as_button_login_n = tk.Button(as_root, text="登录普通账号")
    as_button_login_n.pack(fill='x')
    
    as_button_login_m = tk.Button(as_root, text="登录成员账号")
    as_button_login_m.pack(fill='x')
    
    as_root.mainloop()
main_button_ASetting = tk.Button(main_root, text="更多设置", command=a_setting)
main_button_ASetting.place(relx=0.65, rely=0.50)
main_button_ASetting.place(relwidth=0.30, relheight=0.45)

main_root.mainloop()
