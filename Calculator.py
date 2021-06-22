import tkinter as tk

app = tk.Tk()
app.title("Calculator")
app.geometry('360x490')
app.configure(bg="#002147")
app.resizable(width=False,height=False)
# font
font = ('verdana', 10, 'bold')
# button style
btn_style = {"font": font, "width": 5, "relief": 'ridge', "activebackground": "orange", "activeforeground": 'white'}
btn_gridStyle = {"ipadx": 10, "ipady": 20, "padx": 5, "pady": 3}

history_res = ''
def click_btn_function(event):
    b = event.widget
    t = str(b['text'])
    global history_res
    history_res += t
    outPutBox.delete(0,tk.END)
    outPutBox.insert(tk.END, history_res)


outPutBox = tk.Entry(app, font=('verdana', 18, 'bold'), width=20)
outPutBox.grid(row=0, column=0, columnspan=4, padx=5, pady=20, ipady=20)

temp = 1
for i in range(10, 7, -1):
    for j in range(0, 3):
        btn = tk.Button(app, text=str(temp), **btn_style)
        btn.grid(row=i, column=j, **btn_gridStyle)
        temp = temp + 1
        btn.bind('<Button-1>', click_btn_function)


# equals to
def getAns():
    global history_res
    input_str = outPutBox.get()
    outPutBox.delete(0, tk.END)
    outPutBox.insert(0, eval(history_res))


equlas_to_Btn = tk.Button(app, text="=", **btn_style, command=getAns)
equlas_to_Btn.grid(row=11, column=2, **btn_gridStyle)

# backspace
def backspace():
    global history_res
    history_res = history_res[:-1]
    outPutBox.delete(0, tk.END)
    outPutBox.insert(tk.END, history_res)

backSp_btn = tk.Button(app, text="DEL",**btn_style, command=backspace)
backSp_btn.grid(row=7, column=3, **btn_gridStyle)

def clearAll():
    global history_res
    history_res = ""
    outPutBox.delete(0,tk.END)

clear_all = tk.Button(app, text="CLR", **btn_style, command=clearAll)
clear_all.grid(row=7, column=2,**btn_gridStyle)
#
decimalButton = tk.Button(app, text=".", **btn_style)
decimalButton.grid(row=11, column=0, **btn_gridStyle)
decimalButton.bind('<Button-1>', click_btn_function)
# zero
zeroBtn = tk.Button(app, text='0', **btn_style)
zeroBtn.grid(row=11, column=1, **btn_gridStyle)
zeroBtn.bind('<Button-1>', click_btn_function)
# operator button
plusBtn = tk.Button(app, text="+", **btn_style)
plusBtn.grid(row=8, column=3, **btn_gridStyle)
subBtn = tk.Button(app, text="-", **btn_style)
subBtn.grid(row=9, column=3, **btn_gridStyle)
multiBtn = tk.Button(app, text="/", **btn_style)
multiBtn.grid(row=10, column=3, **btn_gridStyle)
divBtn = tk.Button(app, text="*", **btn_style)
divBtn.grid(row=11, column=3, **btn_gridStyle)
# binding
plusBtn.bind('<Button-1>', click_btn_function)
subBtn.bind('<Button-1>', click_btn_function)
multiBtn.bind('<Button-1>', click_btn_function)
divBtn.bind('<Button-1>', click_btn_function)

tk.mainloop()