import os
import dotenv
import requests
from src.geopoint import geocode
dotenv.load_dotenv()

def middlepoint(point_1,point_2):  
    print((point_1[0]+point_2[0])/2,(point_1[1]+point_2[1])/2)
    return [(point_1[0]+point_2[0])/2,(point_1[1]+point_2[1])/2]

def middle(point_1,point_2):
    point_1=geocode(point_1)["coordinates"]
    point_2=geocode(point_2)["coordinates"]
    middle_point=middlepoint(point_1,point_2)
    return middle_point ,point_1 , point_2

def my_api_call(point_1,point_2 ,tipo = "cafe"):
    key = os.getenv("API_GOOGLE")
    try :
        middle_point, point_1 , point_2 =middle(point_1,point_2)
        lat = middle_point[0]
        long = middle_point[1]
        radius = 500
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={long},{lat}&radius={radius}&type={tipo}&key={key}"
        print(url)
        res = requests.get(url)
        data = res.json()
        print(data["results"][0])
        return str(middle_point[::-1]), str(data["results"][0]), point_1 [::-1], point_2 [::-1],middle_point[::-1]
    except :
        point_1 =[-3.5974614, 40.4030343]
        point_2 =[-3.6127822, 40.4030343]
        middle_point= middlepoint(point_1,point_2)
        print(middle_point)
        lat = middle_point[0]
        long = middle_point[1]
        radius = 500
        url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={long},{lat}&radius={radius}&type={tipo}&key={key}"
        print(url)
        res = requests.get(url)
        data = res.json()
        try:
            middle_point=(list(data["results"][0]["geometry"]["location"].values()))
            print(data["results"][0])
            return str(middle_point[::-1]), str(data["results"][0]), point_1 [::-1], point_2 [::-1],middle_point
        except:
            return str(middle_point[::-1]), str(data["results"]), point_1 [::-1], point_2 [::-1],middle_point[::-1]