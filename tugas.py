import tkinter as tk

def jendelaInput(): 
    def saveInput1():
        a4 = inputA4.get()
        viewerA4.config(state='normal')
        viewerA4.delete(0, 'end')
        viewerA4.insert(0, a4)
        viewerA4.config(state='readonly')
        inputWindow.destroy()
    inputWindow = tk.Tk()
    inputWindow.title("Configuration Paper A4")
    inputWindow.geometry("250x120")
    inputA4 = tk.Entry(inputWindow, justify="center")

    tk.Label(inputWindow, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputA4.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
    
def configPaper2():
    def saveInput2():
        a3 = inputA3.get()
        viewerA3.config(state='normal')
        viewerA3.delete(0, 'end')
        viewerA3.insert(0, a3)
        viewerA3.config(state='readonly')
        inputWindow2.destroy()
    inputWindow2 = tk.Tk()
    inputWindow2.title("Configuration Paper A3")
    inputWindow2.geometry("250x120")
    inputA3 = tk.Entry(inputWindow2, justify="center")

    tk.Label(inputWindow2, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputA3.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow2, text="Save Changes", command=saveInput2).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)
    tk.Button(inputWindow, text="Save Changes", command=saveInput1).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)
    
def configPaper3():
    def saveInput3():
        b1 = inputB1.get()
        viewerB1.config(state='normal')
        viewerB1.delete(0, 'end')
        viewerB1.insert(0, b1)
        viewerB1.config(state='readonly')
        inputWindow3.destroy()
    inputWindow3 = tk.Tk()
    inputWindow3.title("Configuration Paper B1")
    inputWindow3.geometry("250x120")
    inputB1 = tk.Entry(inputWindow3, justify="center")

    tk.Label(inputWindow3, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputB1.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow3, text="Save Changes", command=saveInput3).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)
    
def configPaper4():
    def saveInput4():
        b2 = inputB2.get()
        viewerB2.config(state='normal')
        viewerB2.delete(0, 'end')
        viewerB2.insert(0, b2)
        viewerB2.config(state='readonly')
        inputWindow4.destroy()
    inputWindow4 = tk.Tk()
    inputWindow4.title("Configuration Paper B2")
    inputWindow4.geometry("250x120")
    inputB2 = tk.Entry(inputWindow4, justify="center")

    tk.Label(inputWindow4, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputB2.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow4, text="Save Changes", command=saveInput4).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)    
    
master = tk.Tk()
master.title("Project Akhir")
master.geometry("300x300")

# cek ketersediaan kertas
tk.Label(master, text="Check Paper Availability", font = ('Google Sans','13', 'bold')).grid(row=0, column=0, columnspan = 4)
tk.Label(master, text="A4", font = ('Google Sans','10')).grid(row=1, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=1, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=1, column = 3, sticky=tk.W)

tk.Label(master, text="A3", font = ('Google Sans','10')).grid(row=2, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=2, column = 3, sticky=tk.W)

tk.Label(master, text="B1", font = ('Google Sans','10')).grid(row=3, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=3, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=3, column = 3, sticky=tk.W)

tk.Label(master, text="B2", font = ('Google Sans','10')).grid(row=4, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=4, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=4, column = 3, sticky=tk.W)

# cek ketersediaan Tinta
tk.Label(master, text="Check Ink Availability", font = ('Google Sans','13', 'bold')).grid(row=5, column=0, columnspan = 4, sticky = tk.W)
tk.Label(master, text="Dark", font = ('Google Sans','10')).grid(row=6, rowspan = 2, column=0, sticky=tk.E+tk.N)
tk.Entry(master, justify="left").grid(row=6, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=6, column = 3, sticky=tk.W)

# cek sudah mencetak berapa kali cetak
tk.Label(master, text="Check Number of Prints", font = ('Google Sans','13', 'bold')).grid(row=7, column=0, columnspan = 4, pady = 15, sticky = tk.W)
tk.Label(master, text="Total", font = ('Google Sans','10')).grid(row=8, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=8, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
# tk.Button(master, text = "add").grid(row=8, column = 3, sticky=tk.W)

# Tombol print
tk.Button(master, text = "PRINT", width = 15,  font = ('Google Sans','8', 'bold')).grid(row=9, column = 0, columnspan = 4, pady = 10, sticky=tk.N+tk.E+tk.S+tk.W)

tk.mainloop()
