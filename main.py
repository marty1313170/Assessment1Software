import tkinter as tk
from tkcalendar import DateEntry
import earthquakedata
from tkinter import messagebox
from datetime import datetime, timezone, timedelta

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
        messagebox.showwarning("Missing information, will not continue") # If even location is missing, will not continue
        return
    if magnitude and date_earth == "": # If magnitude and date_earth is missing still continue
        earthquakedata.coords_to_location(location_area)
        return 

    coords = earthquakedata.coords_to_location(location_area)
    if coords is None:
        messagebox.showerror("Error", "Could not find location try again with a vaild input ") # Failed to procceed if location is not found
        return
    
    if date_earth:
       date_ms = datetime.strptime(date_earth, "%d-%m-%Y").replace(tzinfo=timezone.utc).timestamp() * 1000
       start = datetime.strptime(date_earth, "%d-%m-%Y").strftime("%Y-%m-%d")
       end = (datetime.strptime(date_earth, "%d-%m-%Y") + timedelta(days=1)).strftime("%Y-%m-%d")
    else:
       date_ms = None
       start = None
       end = None

       

    lat, lon = coords 
    result, is_fallback = earthquakedata.real_location(lat, lon, date_earth, magnitude, start, end)

    

    
    
    

    features = result["features"]
    exact_area = any(location_area.lower() in ed ["properties"]["place"].lower() for ed in features)
    found_match = False
    for ed in features:
        place =  ed["properties"]["place"]
        mag = ed["properties"]["mag"]
        time = ed["properties"]["time"]
        if date_ms and abs(time - date_ms) < time_closest:
           found_match = True
           listbox.insert(tk.END, f"M{mag} - {place} (matched result)") # It found an exact location 
        elif magnitude and date_earth == "":
             print(result)  
             listbox.insert(tk.END, f"M{mag} - {place} (newest result)") #Newest earthquake
        elif magnitude and abs (float(magnitude) - float (mag)) < closest_result:
             listbox.insert(tk.END, f"M{mag} - {place} (newest result)")
        elif magnitude and date_earth == "":
            print(result) 
        else:
            listbox.insert(tk.END, f"M{mag} - {place}")


    
    if not exact_area and not found_match:
        listbox.insert(0, "Could not find earthquake in exact location ") # If fails to find that specific of a earthquake then just finds a earthquake 500km within input location
        listbox.insert(1, "here are the closest ones")
        
    print(result)




# Below are Visual Widgets 
label_0 = tk.Label(root, text="To search earthquakes on this directory, fill out the location, other inputs such as \n the date and magnitude are optional but recommended for more accurate searches. Leave Date with NO characters if unknown", font=("helvetica", 12))
label_0.place(x=600, y=50)

label_1 = tk.Label(root, text="Welcome to the EarthQUAKE Directory", font=("impact", 32))
label_1.place(x=590, y=-10)


label_2 = tk.Label(root, text="Location of the earthquake?:" ,font=("Arial", 14))
label_2.place(x=750, y=90)

entry_1 = tk.Entry(root, width=30, bg=("blue"))
entry_1.place(x=750, y=120)

button_1 = tk.Button(root, text="Search for this earthquake",  command=call_data_search)
button_1.place(x=750, y=540)

label_2 = tk.Label(root, text="Date of the earthquake" ,font=("Arial", 14))
label_2.place(x=750, y=150)

entry_2 = DateEntry(root, date_pattern='dd-mm-yyyy')
entry_2.place(x=750, y=180)

label_3 = tk.Label(root, text="Magnitude of the earthquake? Up to 1 decimal point")
label_3.place(x=750, y=220)

entry_3 = tk.Entry(root, width=30, bg=("blue"))
entry_3.place(x=750, y=260)

listbox = tk.Listbox(root, width=50,height=10)
listbox.place(x=750, y=340)





root.mainloop()



