import tkinter as tk
from tkcalendar import DateEntry
import earthquakedata
from tkinter import messagebox
from datetime import datetime, timezone

root = tk.Tk()
root.title("Earthquake lookup")
root.geometry("600x400")

closest_result = 0.3

# Function: call backend and API from earthquakedata.py

def call_data_search(closest_result = 0.3, time_closest = 86400000):
    listbox.delete(0, tk.END)
    location_area = entry_1.get()
    date_earth = entry_2.get()
    magnitude = entry_3.get()

    if not location_area:
        messagebox.showwarning("Missing information, will not continue")
        return
    if magnitude and date_earth == "":
        earthquakedata.coords_to_location(location_area)
        return 


    
    coords = earthquakedata.coords_to_location(location_area)
    if coords is None:
        messagebox.showerror("Error")
        return
    
    lat, lon = coords
    result, is_fallback = earthquakedata.real_location(lat, lon, date_earth, magnitude)

    if date_earth:
       date_ms = datetime.strptime(date_earth, "%d-%m-%Y").replace(tzinfo=timezone.utc).timestamp() * 1000
    else:
       date_ms = None

    
    
    

    features = result["features"]
    exact_area = any(location_area.lower() in ed ["properties"]["place"].lower() for ed in features)
    if not exact_area:
        listbox.insert(0, "Could not find earthquake in exact location here are the closest ones!")
    for ed in features:
        place =  ed["properties"]["place"]
        mag = ed["properties"]["mag"]
        time = ed["properties"]["time"]
        if date_ms and abs(time - date_ms) < time_closest:
           listbox.insert(tk.END, f"M{mag} - {place} (matched result)")
        elif magnitude and date_earth == "":
             print(result)  
             listbox.insert(tk.END, f"M{mag} - {place} (newest result)")
        elif magnitude and abs (float(magnitude) - float (mag)) < closest_result:
             listbox.insert(tk.END, f"M{mag} - {place} (newest result)")
        elif magnitude and date_earth == "":
            print(result)
        else:
            listbox.insert(tk.END, f"M{mag} - {place}")
        
        

    
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



