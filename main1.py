#Resource 1(Nutritionix): https://developer.nutritionix.com/
#Resource 2(Sheety): https://sheety.co/
from confidential_data import app_id,app_keys,authorization_header
from datetime import datetime
import requests

headers = {
    "x-app-id":app_id,
    "x-app-key":app_keys,
    # "x-remote-user-id": "0"
}
exercise_endpoints = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_endpoints_parameters = {
    "query":"trekked 3 km",
    "gender":"male",
    "weight_kg":80,
    "height_cm":180,
    "age":30
}
response = requests.post(url = exercise_endpoints, json = exercise_endpoints_parameters, headers = headers)
# print(response.json()["exercises"][0]["name"])
ex_list = response.json()["exercises"]


sheety_post_api = "https://api.sheety.co/98195e6215fa2005ed1c0351410ca88e/workoutTracking/workouts"
headers = {
    "Authorization":authorization_header
}

for item in ex_list:
    sheety_post_api_parameter = {
        "workout":{
            "date":f"{datetime.now().date().strftime('%d/%m/%Y')}",
            "time":f"{datetime.now().time().strftime('%X')}",
            "exercise":f"{item['name'].title()}",
            "duration":f"{item['duration_min']}",
            "calories":f"{item['nf_calories']}"
        }
    }
    response = requests.post(url = sheety_post_api, json = sheety_post_api_parameter, headers = headers)
    print(response.json())
    # print(f"{item['name']} {item['duration_min']} {item['nf_calories']}")
