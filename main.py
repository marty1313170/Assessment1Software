import tkinter as tk

root = tk.Tk()

root.geometry("600x400")

root.grid_columnconfigure(0, weight=1)
frm = tk.Frame(root)
frm.grid()
tk.Label(frm, text="Welcome to the EarthQuake DIRECTORY!!", font=("impact", 24) ).grid(column=0, row=0)
tk.Button(frm, text="Search").grid(column=0, row=2)



entry = tk.Entry(root)
entry.grid(column=2, row=4)


root.mainloop()