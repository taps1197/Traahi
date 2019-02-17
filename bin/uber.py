import os 
import json

from uber_rides.session import Session
from uber_rides.client import UberRidesClient

from pprint import  pprint

session = Session(server_token="P0xeLpEgkQct68R3USut3nBst62X83Tz4V8BT7CR")
client = UberRidesClient(session)


response = client.get_products(37.77, -122.41)
products = response.json.get('products')

with open('data.json','w') as outfile:
    json.dump(products, outfile)

with open('data.json') as inFile:
    data = json.load(inFile)

pprint(data)
