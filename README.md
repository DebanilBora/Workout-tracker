🏋️ Workout Tracker with Nutritionix & Google Sheets

This project is a Workout Tracking App built with Python.
It uses the Nutritionix API to analyze natural language exercise input (e.g., “Ran 3 km and did 20 minutes cycling”) and automatically logs the results (exercise, duration, calories) into a Google Sheet via the Sheety API.

🚀 Features

Accepts exercise input in plain English.

Fetches duration and calories burned automatically from Nutritionix.

Logs workout data (date, time, exercise, duration, calories) into a Google Sheet.

Secures credentials using a .env file.

🛠️ Tech Stack

Python 3.13

Nutritionix API → Natural language exercise parsing

Sheety API → Google Sheets integration

dotenv → Manage API keys securely