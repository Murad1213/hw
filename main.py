import tkinter as tk

clicks = 0
clicks2 = 0
clicks3 = 0


def click_button():
    global clicks
    clicks += 1
    label1.config(text=f" {clicks}")


def click_button1():
    global clicks
    clicks -= 1
    label1.config(text=f" {clicks}")


def click_button2():
    global clicks2
    clicks2 += 1
    label2.config(text=f" {clicks2}")


def click_button3():
    global clicks2
    clicks2 -= 1
    label2.config(text=f" {clicks2}")


def click_button4():
    global clicks3
    clicks3 = clicks2 + clicks
    label5.config(text=f" {clicks3}")


def click_button5():
    global clicks3
    clicks3 = clicks - clicks2
    label5.config(text=f" {clicks3}")


root = tk.Tk()
root.title("James Bond")
root.geometry("400x300+200+500")

btn = tk.Button(
    text="up",
    background="#4b8bad",
    foreground="red",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
    command=click_button
)

btn.place(x=50, y=100)
btn1 = tk.Button(
    text="down",
    background="#4b8bad",
    foreground="red",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
    command=click_button1
)
btn1.place(x=50, y=150)

btn = tk.Button(
    text="up",
    background="#4b8bad",
    foreground="red",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
    command=click_button2
)

btn.place(x=250, y=100)
btn1 = tk.Button(
    text="down",
    background="#4b8bad",
    foreground="red",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
    command=click_button3
)
btn1.place(x=250, y=150)

label1 = tk.Label(
    text="0",
    background="white",
    foreground="black",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
)
label1.place(x=50, y=50)

label2 = tk.Label(
    text="0",
    background="white",
    foreground="black",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
)
label2.place(x=250, y=50)

btn4 = tk.Button(
    text="+",
    background="#4b8bad",
    foreground="red",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
    command=click_button4
)
btn4.place(x=150, y=100)

btn5 = tk.Button(
    text="-",
    background="#4b8bad",
    foreground="red",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
    command=click_button5

)
btn5.place(x=150, y=150)

label5 = tk.Label(
    text="0",
    background="white",
    foreground="black",
    padx="20",
    pady="8",
    font="25",
    height="1",
    width="1",
)
label5.place(x=150, y=200)

root.mainloop()
