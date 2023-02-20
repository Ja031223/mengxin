import tkinter
import random
E1 = None
var = None
window = None


def button_Pushed():
    global window
    window.destroy()


def button_event():
    global var, E1
    a = random.randint(0, 101)
    if E1.get() == a:
        var.set("猜对了")
    else:
        var.set("猜错了")


def main():
    global window, var, E1
    window = tkinter.Tk()
    window.geometry('400x90+600+400')
    window.title('猜数字小游戏-终极版')
    var = tkinter.StringVar()
    var.set("")
    L1 = tkinter.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=15, height=2)
    L1.pack()
    L2 = tkinter.Label(window, text="来玩数字游戏吧")
    L2.pack()
    button_one = tkinter.Button(window, text="猜数字", command=button_event)
    button_one.pack(side='left')
    button_two = tkinter.Button(window, text="退出", command=button_Pushed)
    button_two.pack(side='right')
    E1 = tkinter.Entry(window, bd=5)
    E1.pack()
    window.mainloop()


main()
