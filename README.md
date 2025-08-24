🏋️ Workout Tracker with Nutritionix + Sheety

A Python automation project that tracks your workouts using the Nutritionix API and logs them into Google Sheets via the Sheety API.
This project lets you enter natural language exercise descriptions (like “ran 3 miles and did 30 minutes of yoga”) and automatically records the workout details in a spreadsheet.

🚀 Features

🖊 Accepts natural language input for workouts

🔗 Fetches exercise details (duration, calories, etc.) using Nutritionix API

📊 Automatically logs workouts into Google Sheets via Sheety API

🛡 Secure credentials with .env (no hardcoding API keys)

🧩 Error handling for failed API requests

🛠 Tech Stack

Python 3

requests – API calls

dotenv – environment variable management

Nutritionix API – for workout/exercise parsing

Sheety API – for logging into Google Sheets

⚙️ Setup & Installation
1️⃣ Clone the repository
git clone https://github.com/DebanilBora/Workout-tracker.git
cd workout-tracker

2️⃣ Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install requests python-dotenv

4️⃣ Setup .env file

Create a .env file in the project root with your API credentials:

APP_ID=your_nutritionix_app_id
API_KEY=your_nutritionix_api_key
SHEET_ENDPOINT=https://api.sheety.co/xxxx/workoutTracking/workouts
BEARER_TOKEN=your_sheety_bearer_token

▶️ Usage

Run the script:

python main.py


Type in exercises naturally, e.g.:

ran 5km and did 20 minutes of cycling


The script will:

✅ Send your input to Nutritionix API

📥 Parse exercises with duration & calories

📊 Log each workout in Google Sheets

📝 Example Google Sheet
Date	Time	Exercise	Duration (min)	Calories
24/08/2025	19:45:12	Running	30	250
24/08/2025	19:45:12	Cycling	20	180
⚠️ Disclaimer

This is a learning/portfolio project.

Nutritionix data may not always be 100% accurate.

Use responsibly and double-check for fitness tracking.

🏷 Tags

#Python #API #Automation #WorkoutTracker #GoogleSheets
