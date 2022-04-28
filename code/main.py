import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import requests


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class Page1(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        global Entry1, Entry2

        def Button1_command():
            if Entry1.get() == "Admin" and Entry2.get() == "adminpass":
                print("You Sing as Admin")
                p2.lift()
            elif Entry1.get() == "User" and Entry2.get() == "userpass":
                print("You Sing as User")
                p2.lift()
            elif Entry1.get() == "Guest" and Entry2.get() == "":
                print("You Sing as Guest")
                p2.lift()
            else:
                messagebox.showerror("showinfo", "Wrong Login or Password")

        def Button2_command():
            global Entry1, Entry2
            Entry2.delete(0, tk.END)
            Entry1.delete(0, tk.END)

        self.image = Image.open('img/chatbg.png').resize((600, 500))
        self.python_image = ImageTk.PhotoImage(self.image)

        canvas_loginpage = tk.Canvas(self, width=600,
                                     height=500)
        canvas_loginpage.create_image(0, 0, image=self.python_image,
                                      anchor="nw")
        canvas_loginpage.pack(fill="both", expand=1)
        canvas_loginpage.create_text(300, 80, font=("Times", 28), text="Виртуальный Ассистент")
        canvas_loginpage.create_text(310, 155, font=("Times", 10), text="Enter Login")
        canvas_loginpage.create_text(300, 215, font=("Times", 10), text="Enter Password")

        Entry1 = tk.Entry(self)
        Entry1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        Entry1["font"] = ft
        Entry1["fg"] = "#333333"
        Entry1["justify"] = "center"
        Entry1.place(x=360, y=140, width=145, height=30)

        Button1 = tk.Button(self)
        Button1["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times', size=10)
        Button1["font"] = ft
        Button1["fg"] = "#000000"
        Button1["justify"] = "center"
        Button1["text"] = "Log In"
        Button1["cursor"] = "mouse"
        Button1["command"] = Button1_command
        Button1.place(x=300, y=260, width=70, height=25)

        Button2 = tk.Button(self)
        Button2["bg"] = "#e14141"
        ft = tkFont.Font(family='Times', size=10)
        Button2["font"] = ft
        Button2["fg"] = "#000000"
        Button2["justify"] = "center"
        Button2["text"] = "Clear"
        Button2["cursor"] = "mouse"
        Button2["command"] = Button2_command
        Button2.place(x=430, y=260, width=70, height=25)

        Entry2 = tk.Entry(self)
        Entry2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        Entry2["font"] = ft
        Entry2["fg"] = "#333333"
        Entry2["justify"] = "center"
        Entry2["show"] = "*"
        Entry2.place(x=360, y=200, width=146, height=30)


class Page2(Page):

    def __init__(self, *args, **kwargs):

        Page.__init__(self, *args, **kwargs)
        self.image = Image.open('img/bg1.jpg').resize((600, 500))
        self.python_image = ImageTk.PhotoImage(self.image)

        canvas_menupage = tk.Canvas(self, width=600,
                                    height=500)
        canvas_menupage.create_image(0, 0, image=self.python_image,
                                     anchor="nw")
        canvas_menupage.pack(fill="both", expand=1)
        canvas_menupage.create_text(450, 380, font=("Times", 30), text="Menu")

        def GButton_949_command():
            p1.lift()

        def GButton_67_command():
            if Entry1.get() == "Admin" and Entry2.get() == "adminpass":
                p5.lift()
            elif Entry1.get() == "User" and Entry2.get() == "userpass":
                p5.lift()
            else:
                print("access blocked")
                messagebox.showerror("showinfo", "access blocked")

        def GButton_604_command():
            p6.lift()

        def GButton_140_command():
            p4.lift()

        def GButton_557_command():
            if Entry1.get() == "Admin" and Entry2.get() == "adminpass":
                p3.lift()
            elif Entry1.get() == "User" and Entry2.get() == "userpass":
                p3.lift()
            else:
                print("access blocked")
                messagebox.showerror("showinfo", "access blocked")

        GButton_949 = tk.Button(self)
        GButton_949["bg"] = "#f43c3c"
        ft = tkFont.Font(family='Times', size=10)
        GButton_949["font"] = ft
        GButton_949["fg"] = "#000000"
        GButton_949["justify"] = "center"
        GButton_949["text"] = "Back"
        GButton_949.place(x=30, y=360, width=107, height=30)
        GButton_949["command"] = GButton_949_command

        GButton_67 = tk.Button(self)
        GButton_67["bg"] = "#ffd700"
        ft = tkFont.Font(family='Times', size=10)
        GButton_67["font"] = ft
        GButton_67["fg"] = "#000000"
        GButton_67["justify"] = "center"
        GButton_67["text"] = "Калькулятор"
        GButton_67.place(x=340, y=20, width=205, height=151)
        GButton_67["command"] = GButton_67_command

        GButton_604 = tk.Button(self)
        GButton_604["bg"] = "#01aaed"
        ft = tkFont.Font(family='Times', size=10)
        GButton_604["font"] = ft
        GButton_604["fg"] = "#000000"
        GButton_604["justify"] = "center"
        GButton_604["text"] = "Время"
        GButton_604.place(x=340, y=190, width=203, height=149)
        GButton_604["command"] = GButton_604_command

        GButton_140 = tk.Button(self)
        GButton_140["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times', size=10)
        GButton_140["font"] = ft
        GButton_140["fg"] = "#000000"
        GButton_140["justify"] = "center"
        GButton_140["text"] = "Погода"
        GButton_140.place(x=50, y=190, width=205, height=150)
        GButton_140["command"] = GButton_140_command

        GButton_557 = tk.Button(self)
        GButton_557["bg"] = "#00ced1"
        ft = tkFont.Font(family='Times', size=10)
        GButton_557["font"] = ft
        GButton_557["fg"] = "#000000"
        GButton_557["justify"] = "center"
        GButton_557["text"] = "Банкомат"
        GButton_557.place(x=50, y=20, width=204, height=149)
        GButton_557["command"] = GButton_557_command


class Page3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.image = Image.open('img/atm_bg.jpg').resize((600, 500))
        self.python_image = ImageTk.PhotoImage(self.image)

        canvas1 = tk.Canvas(self, width=600,
                            height=500)
        canvas1.create_image(0, 0, image=self.python_image,
                             anchor="nw")
        canvas1.pack(fill="both", expand=1)
        canvas1.create_text(300, 100, font=("Times", 30), text="Банкомат")

        class bankomat:
            def __init__(self, balance):
                self.__balance = balance

            def print_balance(self):
                return self.__balance

            def add_balance(self, balance):
                self.__balance += balance

            def min_balance(self, balance):
                self.__balance -= balance

        def GButton_163_command():
            s.add_balance(int(GLineEdit_474.get()))
            canvas1.itemconfig("balance", text="Balance: " + str(s.print_balance()))
            GLineEdit_474.delete(0, "end")

        def GButton_218_command():
            s.min_balance(int(GLineEdit_330.get()))
            canvas1.itemconfig("balance", text="Balance: " + str(s.print_balance()))
            GLineEdit_330.delete(0, "end")

        def GButton_811_command():
            p2.lift()

        s = bankomat(0)

        canvas1.create_text(150, 200, font=("Times", 10), text=f"Balance:{s.print_balance()}", tag="balance")
        canvas1.create_text(150, 250, font=("Times", 10), text="Withdraw")
        canvas1.create_text(150, 350, font=("Times", 10), text="Deposit")

        GLineEdit_474 = tk.Entry(self)
        GLineEdit_474["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_474["font"] = ft
        GLineEdit_474["fg"] = "#333333"
        GLineEdit_474["justify"] = "center"
        GLineEdit_474["text"] = ""
        GLineEdit_474.place(x=250, y=240, width=101, height=30)

        GButton_163 = tk.Button(self)
        GButton_163["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times', size=10)
        GButton_163["font"] = ft
        GButton_163["fg"] = "#000000"
        GButton_163["justify"] = "center"
        GButton_163["text"] = "Confirm"
        GButton_163.place(x=350, y=240, width=88, height=30)
        GButton_163["command"] = GButton_163_command

        GButton_218 = tk.Button(self)
        GButton_218["bg"] = "#5fb878"
        ft = tkFont.Font(family='Times', size=10)
        GButton_218["font"] = ft
        GButton_218["fg"] = "#000000"
        GButton_218["justify"] = "center"
        GButton_218["text"] = "Confirm"
        GButton_218.place(x=350, y=340, width=88, height=30)
        GButton_218["command"] = GButton_218_command

        GLineEdit_330 = tk.Entry(self)
        GLineEdit_330["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_330["font"] = ft
        GLineEdit_330["fg"] = "#333333"
        GLineEdit_330["justify"] = "center"
        GLineEdit_330["text"] = ""
        GLineEdit_330.place(x=250, y=340, width=99, height=30)

        GButton_811 = tk.Button(self)
        GButton_811["bg"] = "#f53d3d"
        ft = tkFont.Font(family='Times', size=10)
        GButton_811["font"] = ft
        GButton_811["fg"] = "#000000"
        GButton_811["justify"] = "center"
        GButton_811["text"] = "Back"
        GButton_811.place(x=100, y=400, width=92, height=30)
        GButton_811["command"] = GButton_811_command


class Page4(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def GButton_81_command():
            p2.lift()

        def get_weather():
            city = cityEdit.get()
            key = "c5204b84b9264b0b806a7474bd6a40c9"
            url = 'http://api.openweathermap.org/data/2.5/weather'
            params = {'APPID': key, 'q': city, 'units': 'metric'}
            result = requests.get(url, params=params)
            weather = result.json()
            canvas1.itemconfig(info, text=f'{str(weather["name"])}:{weather["main"]["temp"]} С')

        self.image = Image.open('img/weather_bg.jpeg').resize((600, 500))
        self.python_image = ImageTk.PhotoImage(self.image)
        canvas1 = tk.Canvas(self, width=600,
                            height=500)
        canvas1.create_image(0, 0, image=self.python_image,
                             anchor="nw")
        canvas1.pack(fill="both", expand=1)

        cityEdit = tk.Entry(self, bg='white', font=30)
        cityEdit.place(x=250, y=200)
        btn = tk.Button(self, text='Узнать', command=get_weather)
        btn.place(x=310, y=300)
        info = canvas1.create_text(350, 100, font=("Times", 20, "bold"), text='Погодная информация', fill='red')

        GButton_81 = tk.Button(self)
        GButton_81["bg"] = "#f53d3d"
        ft = tkFont.Font(family='Times', size=10)
        GButton_81["font"] = ft
        GButton_81["fg"] = "#000000"
        GButton_81["justify"] = "center"
        GButton_81["text"] = "Back"
        GButton_81.place(x=20, y=360, width=92, height=30)
        GButton_81["command"] = GButton_81_command


class Page5(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.image = Image.open('img/calc.jpg').resize((600, 500))
        self.python_image = ImageTk.PhotoImage(self.image)

        def GButton_870_command():
            GLineEdit_222.insert("end", 7)

        def GButton_719_command():
            GLineEdit_222.insert("end", 6)

        def GButton_446_command():
            GLineEdit_222.insert("end", 9)

        def GButton_774_command():
            GLineEdit_222.insert("end", "*")

        def GButton_597_command():
            GLineEdit_222.insert("end", 4)

        def GButton_190_command():
            GLineEdit_222.insert("end", 1)

        def GButton_757_command():
            GLineEdit_222.insert("end", 8)

        def GButton_830_command():
            GLineEdit_222.insert("end", 5)

        def GButton_982_command():
            GLineEdit_222.insert("end", "-")

        def GButton_278_command():
            GLineEdit_222.insert("end", 2)

        def GButton_78_command():
            GLineEdit_222.insert("end", 3)

        def GButton_998_command():
            GLineEdit_222.delete(0, "end")

        def GButton_13_command():
            GLineEdit_222.delete(len(GLineEdit_222.get()) - 1, "end")

        def GButton_733_command():
            GLineEdit_222.insert("end", "+")

        def GButton_886_command():
            GLineEdit_222.insert("end", "/")

        def GButton_525_command():
            GLineEdit_222.insert("end", 0)

        def GButton_893_command():
            x = GLineEdit_222.get()
            GLineEdit_222.delete(0, "end")
            GLineEdit_222.insert("end", eval(x))

        def GButton_229_command():
            GLineEdit_222.insert("end", ".")

        def GButton_130_command():
            p2.lift()
        def btn_convers_command():
            p8.lift()     

        canvas1 = tk.Canvas(self, width=600,
                            height=500)
        canvas1.create_image(0, 0, image=self.python_image,
                             anchor="nw")
        canvas1.pack(fill="both", expand=1)
        canvas1.create_text(310, 50, font=("Times", 28), text="Калькулятор",fill="red")
        GLineEdit_222 = tk.Entry(self)
        GLineEdit_222["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=20)
        GLineEdit_222["font"] = ft
        GLineEdit_222["fg"] = "#333333"
        GLineEdit_222["justify"] = "center"
        GLineEdit_222["text"] = "Entry"
        GLineEdit_222.place(x=150, y=80, width=326, height=45)

        GButton_870 = tk.Button(self)
        GButton_870["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_870["font"] = ft
        GButton_870["fg"] = "#000000"
        GButton_870["justify"] = "center"
        GButton_870["text"] = "7"
        GButton_870.place(x=150, y=190, width=77, height=56)
        GButton_870["command"] = GButton_870_command

        GButton_719 = tk.Button(self)
        GButton_719["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_719["font"] = ft
        GButton_719["fg"] = "#000000"
        GButton_719["justify"] = "center"
        GButton_719["text"] = "6"
        GButton_719.place(x=310, y=250, width=77, height=56)
        GButton_719["command"] = GButton_719_command

        GButton_446 = tk.Button(self)
        GButton_446["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_446["font"] = ft
        GButton_446["fg"] = "#000000"
        GButton_446["justify"] = "center"
        GButton_446["text"] = "9"
        GButton_446.place(x=310, y=190, width=77, height=56)
        GButton_446["command"] = GButton_446_command

        GButton_774 = tk.Button(self)
        GButton_774["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_774["font"] = ft
        GButton_774["fg"] = "#000000"
        GButton_774["justify"] = "center"
        GButton_774["text"] = "*"
        GButton_774.place(x=400, y=190, width=77, height=56)
        GButton_774["command"] = GButton_774_command

        GButton_597 = tk.Button(self)
        GButton_597["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_597["font"] = ft
        GButton_597["fg"] = "#000000"
        GButton_597["justify"] = "center"
        GButton_597["text"] = "4"
        GButton_597.place(x=150, y=250, width=77, height=56)
        GButton_597["command"] = GButton_597_command

        GButton_190 = tk.Button(self)
        GButton_190["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_190["font"] = ft
        GButton_190["fg"] = "#000000"
        GButton_190["justify"] = "center"
        GButton_190["text"] = "1"
        GButton_190.place(x=150, y=310, width=77, height=56)
        GButton_190["command"] = GButton_190_command

        GButton_757 = tk.Button(self)
        GButton_757["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_757["font"] = ft
        GButton_757["fg"] = "#000000"
        GButton_757["justify"] = "center"
        GButton_757["text"] = "8"
        GButton_757.place(x=230, y=190, width=77, height=56)
        GButton_757["command"] = GButton_757_command

        GButton_830 = tk.Button(self)
        GButton_830["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_830["font"] = ft
        GButton_830["fg"] = "#000000"
        GButton_830["justify"] = "center"
        GButton_830["text"] = "5"
        GButton_830.place(x=230, y=250, width=77, height=56)
        GButton_830["command"] = GButton_830_command

        GButton_982 = tk.Button(self)
        GButton_982["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_982["font"] = ft
        GButton_982["fg"] = "#000000"
        GButton_982["justify"] = "center"
        GButton_982["text"] = "-"
        GButton_982.place(x=400, y=250, width=77, height=56)
        GButton_982["command"] = GButton_982_command

        GButton_278 = tk.Button(self)
        GButton_278["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_278["font"] = ft
        GButton_278["fg"] = "#000000"
        GButton_278["justify"] = "center"
        GButton_278["text"] = "2"
        GButton_278.place(x=230, y=310, width=77, height=56)
        GButton_278["command"] = GButton_278_command

        GButton_78 = tk.Button(self)
        GButton_78["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_78["font"] = ft
        GButton_78["fg"] = "#000000"
        GButton_78["justify"] = "center"
        GButton_78["text"] = "3"
        GButton_78.place(x=310, y=310, width=77, height=56)
        GButton_78["command"] = GButton_78_command

        GButton_998 = tk.Button(self)
        GButton_998["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_998["font"] = ft
        GButton_998["fg"] = "#000000"
        GButton_998["justify"] = "center"
        GButton_998["text"] = "C"
        GButton_998.place(x=150, y=130, width=77, height=56)
        GButton_998["command"] = GButton_998_command

        GButton_13 = tk.Button(self)
        GButton_13["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_13["font"] = ft
        GButton_13["fg"] = "#000000"
        GButton_13["justify"] = "center"
        GButton_13["text"] = "DEL"
        GButton_13.place(x=310, y=130, width=77, height=56)
        GButton_13["command"] = GButton_13_command

        GButton_733 = tk.Button(self)
        GButton_733["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_733["font"] = ft
        GButton_733["fg"] = "#000000"
        GButton_733["justify"] = "center"
        GButton_733["text"] = "+"
        GButton_733.place(x=400, y=310, width=77, height=56)
        GButton_733["command"] = GButton_733_command

        GButton_886 = tk.Button(self)
        GButton_886["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_886["font"] = ft
        GButton_886["fg"] = "#000000"
        GButton_886["justify"] = "center"
        GButton_886["text"] = "/"
        GButton_886.place(x=400, y=130, width=77, height=56)
        GButton_886["command"] = GButton_886_command

        GButton_525 = tk.Button(self)
        GButton_525["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_525["font"] = ft
        GButton_525["fg"] = "#000000"
        GButton_525["justify"] = "center"
        GButton_525["text"] = "0"
        GButton_525.place(x=230, y=370, width=77, height=56)
        GButton_525["command"] = GButton_525_command

        GButton_893 = tk.Button(self)
        GButton_893["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=10)
        GButton_893["font"] = ft
        GButton_893["fg"] = "#000000"
        GButton_893["justify"] = "center"
        GButton_893["text"] = "="
        GButton_893["relief"] = "flat"
        GButton_893.place(x=400, y=370, width=77, height=56)
        GButton_893["command"] = GButton_893_command

        GButton_229 = tk.Button(self)
        GButton_229["bg"] = "#efefef"
        ft = tkFont.Font(family='Times', size=18)
        GButton_229["font"] = ft
        GButton_229["fg"] = "#000000"
        GButton_229["justify"] = "center"
        GButton_229["text"] = ","
        GButton_229.place(x=310, y=370, width=77, height=56)
        GButton_229["command"] = GButton_229_command

        GButton_130 = tk.Button(self)
        GButton_130["bg"] = "#f53d3d"
        ft = tkFont.Font(family='Times', size=10)
        GButton_130["font"] = ft
        GButton_130["fg"] = "#000000"
        GButton_130["justify"] = "center"
        GButton_130["text"] = "Back"
        GButton_130.place(x=30, y=380, width=92, height=30)
        GButton_130["command"] = GButton_130_command
        btn_convers = tk.Button(self)
        btn_convers ["bg"] = "#f53d3d"
        ft = tkFont.Font(family='Times', size=10)
        btn_convers ["font"] = ft
        btn_convers ["fg"] = "#000000"
        btn_convers ["justify"] = "center"
        btn_convers ["text"] = "Conversion"
        btn_convers .place(x=30, y=300, width=92, height=30)
        btn_convers ["command"] = btn_convers_command 


class Page6(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.image = Image.open('img/bg.gif').resize((600, 500))
        self.python_image = ImageTk.PhotoImage(self.image)

        canvas1 = tk.Canvas(self, width=600,
                            height=500)
        canvas1.create_image(0, 0, image=self.python_image,
                             anchor="nw")
        canvas1.place(x=0, y=0)
        canvas1.create_text(300, 101, font=("Times", 15, "bold"), fill="red",
                            text="hours        minutes        seconds")
        canvas1.create_text(300, 55, font=("Times", 25, "bold"), fill="red", text="Часы")

        def timing():
            # display current hour,minute,seconds
            current_time = time.strftime("%H : %M : %S")
            # configure the clock
            canvas1.itemconfig(clock, text=current_time)
            # clock will change after every 200 microseconds
            canvas1.after(200, timing)

        clock = canvas1.create_text(300, 150, font=("Times", 50), fill="red")

        timing()

        def Button_Back_command():
            p2.lift()

        Button_Back = tk.Button(self)
        Button_Back["bg"] = "#f53d3d"
        ft = tkFont.Font(family='Times', size=10)
        Button_Back["font"] = ft
        Button_Back["fg"] = "#000000"
        Button_Back["justify"] = "center"
        Button_Back["text"] = "Back"
        Button_Back.place(x=20, y=360, width=92, height=30)
        Button_Back["command"] = Button_Back_command


class Page7(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)

        def Button_Back_command():
            p2.lift()

        self.image = Image.open('img/secret.jpg').resize((600, 500))
        self.image2 = Image.open('img/rabbit.jpeg').resize((100, 50))
        self.python_image = ImageTk.PhotoImage(self.image)
        self.python_image2 = ImageTk.PhotoImage(self.image2)

        canvas1 = tk.Canvas(self, width=600,
                            height=500)
        canvas1.create_image(0, 0, image=self.python_image,
                             anchor="nw")
        canvas1.create_image(500, 425, image=self.python_image2)
        canvas1.pack(fill="both", expand=1)
        canvas1.create_text(300, 100, font=("Times", 15), text="Поздравляю вы попали на секретную страницу\n"
                                                               "Тут живет Саблезубый кролик\n"
                                                               "Не трогайте его",fill="white")
        Button_Back = tk.Button(self)
        Button_Back["bg"] = "#f53d3d"
        ft = tkFont.Font(family='Times', size=10)
        Button_Back["font"] = ft
        Button_Back["fg"] = "#000000"
        Button_Back["justify"] = "center"
        Button_Back["text"] = "Back"
        Button_Back.place(x=20, y=400, width=92, height=30)
        Button_Back["command"] = Button_Back_command

        ft = tkFont.Font(family='Times', size=10)
class Page8(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.image = Image.open('img/calc.jpg').resize((600, 500))
        self.python_image = ImageTk.PhotoImage(self.image)
        def Button_Back_command():
            p2.lift()
        def convert():
            rub=int((e1.get()))*76
            
            
            
            canvas1.itemconfig(usd_rub,text=rub)
        def convert1():
            usd=int((e2.get()))/76
            canvas1.itemconfig(rub_usd,text=usd)
        def convert2():
            eur=int((e3.get()))*87
            canvas1.itemconfig(usd_eur,text=eur)
        def convert3():
            som=int((e4.get()))*10900
            canvas1.itemconfig(usd_som,text=som)
        def convert4():
            soom=int((e5.get()))/10900
            canvas1.itemconfig(som_usd,text=soom)


               
        canvas1 = tk.Canvas(self, width=600,
                            height=500)
        canvas1.create_image(0, 0, image=self.python_image,
                             anchor="nw")
        canvas1.pack(fill="both", expand=1)
        canvas1.create_text(310, 50, font=("Times", 28), text="Конвертер",fill="red")
        usd_rub=canvas1.create_text(370, 100, font=("Times", 15), text="usd_rub: ",fill="red")
        rub_usd=canvas1.create_text(370, 140, font=("Times", 15), text="rub_usd: ",fill="red")
        usd_eur=canvas1.create_text(370, 180, font=("Times", 15), text="usd_eur: ",fill="red")
        usd_som=canvas1.create_text(370, 220, font=("Times", 15), text="usd_som: ",fill="red")
        som_usd=canvas1.create_text(370, 260, font=("Times", 15), text="som_usd: ",fill="red")
        
        e1 = tk.Entry(canvas1)       
        e2 = tk.Entry(canvas1)       
        e3 = tk.Entry(canvas1)       
        e4 = tk.Entry(canvas1)       
        e5 = tk.Entry(canvas1)       
        bnt_convers=tk.Button(canvas1,text="usd_rub",command=convert).place(x=20,y=360,width=92,height=30)
        bnt_convers1=tk.Button(canvas1,text="rub_usd",command=convert1).place(x=120,y=360,width=92,height=30)
        bnt_convers2=tk.Button(canvas1,text="rub_usd",command=convert2).place(x=220,y=360,width=92,height=30)
        bnt_convers3=tk.Button(canvas1,text="rub_usd",command=convert3).place(x=320,y=360,width=92,height=30)
        bnt_convers4=tk.Button(canvas1,text="rub_usd",command=convert4).place(x=420,y=360,width=92,height=30)
        canvas1.create_window(160,100,window=e1)
        canvas1.create_window(160,140,window=e2)
        canvas1.create_window(160,180,window=e3)
        canvas1.create_window(160,220,window=e4)
        canvas1.create_window(160,260,window=e5)
        Button_Back = tk.Button(self)
        Button_Back["bg"] = "#f53d3d"
        ft = tkFont.Font(family='Times', size=10)
        Button_Back["font"] = ft
        Button_Back["fg"] = "#000000"
        Button_Back["justify"] = "center"
        Button_Back["text"] = "Back"
        Button_Back.place(x=20, y=400, width=92, height=30)
        Button_Back["command"] = Button_Back_command

        
class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        global p1, p2, p3, p4, p5, p6, p7, p8
        p1 = Page1(self)
        p2 = Page2(self)
        p3 = Page3(self)
        p4 = Page4(self)
        p5 = Page5(self)
        p6 = Page6(self)
        p7 = Page7(self)
        p8 = Page8(self)


        buttonframe = tk.Frame(self)
        container = tk.Frame(self)

        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)



        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # кнопки для быстрого перемещения по страницам
        """
        b1 = tk.Button(buttonframe, text="Page 1", command=p1.lift)
        b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)
        b3 = tk.Button(buttonframe, text="Page 3", command=p3.lift)
        b4 = tk.Button(buttonframe, text="Page 4", command=p4.lift)
        b5 = tk.Button(buttonframe, text="Page 5", command=p5.lift)
        b6 = tk.Button(buttonframe, text="Page 6", command=p6.lift)
        b7 = tk.Button(buttonframe, text="Page 7", command=p7.lift)
        b8 = tk.Button(buttonframe, text="Page 8", command=p8.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")
        b4.pack(side="left")
        b5.pack(side="left")
        b6.pack(side="left")
        b7.pack(side="left")
        b8.pack(side="left")
        """
        p1.show()


if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x510")

    root.title("Виртуальный ассистент")
    root.mainloop()

