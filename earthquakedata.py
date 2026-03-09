import requests

BASE_URL = "https://earthquake.usgs.gov/fdsnws/event/1/query"

OPEN_MAP = "https://nominatim.openstreetmap.org/search?q={place}&format=json&limit=1"

head = {'User-Agent' : "school"}

closest_info = 0.5

def coords_to_location(place, closest=5):

    response = requests.get(
        OPEN_MAP,
        params={"q": place},
        headers=head
    )
    data = response.json()

    if  data:
        print("Not found")
        return None

    
    lat = float(data[0]["lat"])
    lon = float(data[0]["lon"])  
    print(f"Lat: {lat}, Lon: {lon}")
    return lat, lon

def real_location(lat, lon):


    
    response_2 = requests.get(
        BASE_URL,
        params={"latitude": lat, "longitude": lon,  "format": "geojson" , "limit" : 1, "maxradiuskm" : 100,}
    )

    
    data_2 = response_2.json()

    if not data_2:
        print("Not found")
        return None

   
    return data_2




    


    






        




    







