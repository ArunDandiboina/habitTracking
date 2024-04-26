import requests
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

# share,put,post,get.
USER_NAME = os.environ.get("USER_NAME")
TOKEN = os.environ.get("TOKEN")
GRAPH_ID = os.environ.get("GRAPH_ID")
pix_end = "https://pixe.la/v1/users"
print(USER_NAME)

parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# FIRST TIME ONLY
# res = requests.post(url=pix_end,json=parameters)
# print(res.text)

graph_endpoint = f"{pix_end}/{USER_NAME}/graphs"
header = {
    "X-USER-TOKEN": TOKEN
}
data = {
    "id": GRAPH_ID,
    "name": "Cycling graph",   # graph name
    "unit": "Km",              # units
    "type": "float",           # type
    "color": "ajisai"          # color
}

# FIRST TIME ONLY (when creating graph for first time)
# res = requests.post(url=graph_endpoint, json=data, headers=header)
# print(res.text)

date = dt.datetime.now().strftime("%Y%m%d")
print(date)

# post pixel
pixel_end = f"{pix_end}/{USER_NAME}/graphs/{GRAPH_ID}"
pixe_pa = {
    "date": date,
    "quantity":input("how many kilometers did you cycle: ")
}
res = requests.post(url=pixel_end,json=pixe_pa,headers=header)
print(res.text)

# today = dt.datetime(year=2024,month=1,day=18)
# today = today.strftime("%Y%m%d")
# pixel_end_up = f"{pix_end}/{USER_NAME}/graphs/{GRAPH_ID}/{today}"
# pixe_pa_up = {
#     "quantity":"50"
# }
# res = requests.put(url=pixel_end_up,json=pixe_pa_up,headers=header)
# print(res.text)
