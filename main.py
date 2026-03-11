import tkinter as tk
from tkcalendar import DateEntry
import earthquakedata
from tkinter import messagebox

root = tk.Tk()
root.title("Earthquake lookup")
root.geometry("600x400")

# Function: call backend and API from earthquakedata.py

def call_data_search():
    location_area = entry_1.get()
    date_earth = entry_2.get()
    magnitude = entry_3.get()

    if not location_area:
        messagebox.showwarning("Missing information, will not continue")
        return

    
    coords = earthquakedata.coords_to_location(location_area)
    if coords is None:
        messagebox.showerror("Error")
        return

    lat, lon = coords
    result, is_fallback = earthquakedata.real_location(lat, lon, date_earth, magnitude)

    if is_fallback:
        print("Could not find exact earthquake based off your information, here are the closest results")

    features = result["features"]
    for ed in features:
        place =  ed["properties"]["place"]
        mag = ed["properties"]["mag"]
        time = ed["properties"]["time"]
        listbox.insert(tk.END,  f"M{mag} - {place}")

    
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

listbox = tk.Listbox(root, width=50,height=10)
listbox.place(x=50, y=20)





root.mainloop()



