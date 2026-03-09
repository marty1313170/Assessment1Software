import tkinter as tk
from tkcalendar import DateEntry
import earthquakedata
from tkinter import messagebox

root = tk.Tk()
root.title("Earthquake lookup")
root.geometry("600x400")

# Function: call backend and API from earthquakedata.py

def call_data_search(closest=5):
    location_area = entry_1.get()
    date_earth = entry_2.get()
    magnitude = entry_3.get()

    if not location_area:
        messagebox.showwarning("Missing information, will not continue")
        return

    
    if location_area and date_earth and magnitude:
        try:
            val = float(magnitude)
        except ValueError:
            return "Improper value"

    close = min(options, key=lambda x: abs(x - val))

    if abs(closest - val) <= threshold:
        return closest
    else:
        return earthquakedata

        

    result_from_main = earthquakedata.coords_to_location(location_area)

    if result_from_main is None:
        messagebox.showwarning("Not Found")

    lat, lon = result_from_main
    result = earthquakedata.real_location(lat, lon)
    print(result)


    


# Below are Visual Widgets 

label_1 = tk.Label(root, text="Welcome to the EarthQUAKE Directory", font=("impact", 32))
label_1.place(x=440, y=0)


label_2 = tk.Label(root, text="Location of the earthquake?:" ,font=("Arial", 14))
label_2.place(x=540, y=50)

entry_1 = tk.Entry(root, width=30, bg=("blue"))
entry_1.place(x=540, y=80)

button_1 = tk.Button(root, text="Search for this earthquake",  command=call_data_search)
button_1.place(x=585, y=400)

label_2 = tk.Label(root, text="Date of the earthquake" ,font=("Arial", 14))
label_2.place(x=540, y=110)

entry_2 = DateEntry(root, date_pattern='dd-mm-yyyy')
entry_2.place(x=540, y=140)

label_3 = tk.Label(root, text="Magnitude of the earthquake? Up to 1 decimal point")
label_3.place(x=540, y=180)

entry_3 = tk.Entry(root, width=30, bg=("blue"))
entry_3.place(x=540, y=220)


root.mainloop()



