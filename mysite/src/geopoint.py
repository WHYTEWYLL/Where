import requests

def geocode(address):
    res = requests.get(f"https://geocode.xyz/{address}", params={"json":1})
    data = res.json()
    return {
        "type":"Point",
        "coordinates":[float(data["longt"]),float(data["latt"])]
    }