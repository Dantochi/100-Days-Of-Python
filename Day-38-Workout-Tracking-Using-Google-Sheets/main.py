import requests, os
from datetime import datetime
from requests.auth import HTTPBasicAuth
APP_ID = "16da9fbc"
API_KEY = "69518221b9e0e12de534199d11917985"
SHEET_ENDPOINT = "https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/workoutTracking/workouts"
SHEET_PASSWORD = 'jbdjcblwdj'
SHEET_AUTH = "Basic RGFudG9jaGk6amJkamNibHdkag=="
os.environ["APP_ID"] =APP_ID
os.environ["API_KEY"] = API_KEY
os.environ["SHEET_ENDPOINT"] = SHEET_ENDPOINT
os.environ["SHEET_PASSWORD"] = SHEET_PASSWORD
os.environ["SHEET_AUTH"] = SHEET_AUTH
# APP_ID = os.environ["APP_ID"]
# print(APP_ID)
date_today = datetime.now().strftime("%x")
current_time = datetime.now().strftime("%X")
exercise_input = input("What did you do today? ")
print(os.environ)
HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
PARAMETERS = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": 73,
    "age": 25
}
basic = HTTPBasicAuth('Dantochi', 'jbdjcblwdj')
response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=PARAMETERS, headers=HEADERS)
data = response.json()
exercise_data = data["exercises"][0]
exercise = exercise_data["name"].title()
duration = round(exercise_data["duration_min"])
calories = round(exercise_data["nf_calories"])
print(exercise, duration, calories)

SHEET_PARAMETERS = {
    "workout": {
        "date": date_today,
        "time": current_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
SHEET_HEADER = {
    "Authorization": "Basic RGFudG9jaGk6amJkamNibHdkag=="
}


sheet_post = requests.post(url="https://api.sheety.co/5ffbfe8544b47a25bfc91c1a72816097/workoutTracking/workouts",
                           json=SHEET_PARAMETERS, headers=SHEET_HEADER, auth=basic)
print(response.text)
print(sheet_post.status_code)






