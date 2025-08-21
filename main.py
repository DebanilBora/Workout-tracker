import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Clear the terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Load environment variables
load_dotenv()

# Get credentials from .env
APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
SHEET_ENDPOINT = os.getenv("SHEET_ENDPOINT")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Verify required keys exist
if not all([APP_ID, API_KEY, SHEET_ENDPOINT, BEARER_TOKEN]):
    raise ValueError("Missing one or more environment variables.")

# Headers for Nutritionix
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

# Get user input
query = input("Enter the exercises you did today: ")

user_profile = {
    "query": query,
    "gender": "male",
    "weight_kg": 70,
    "height_cm": 175,
    "age": 25
}

# Send to Nutritionix
try:
    response = requests.post("https://trackapi.nutritionix.com/v2/natural/exercise", json=user_profile, headers=nutritionix_headers)
    response.raise_for_status()
    exercises = response.json()["exercises"]
except requests.exceptions.RequestException as e:
    print(f"Error with Nutritionix API: {e}")
    exit()

# Date and time
today_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

# Headers for Sheety
sheety_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}",
    "Content-Type": "application/json"
}

# Post each workout to Sheety
for exercise in exercises:
    sheet_data = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    try:
        response = requests.post(SHEET_ENDPOINT, json=sheet_data, headers=sheety_headers)
        response.raise_for_status()
        print(f"Logged: {sheet_data['workout']['exercise']}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending to Sheety: {e}")
