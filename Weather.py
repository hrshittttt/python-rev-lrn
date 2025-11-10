import requests
from datetime import datetime, timedelta

today = datetime.now()
week_ago = today - timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()

time_data = data["daily"]["time"]
max_data = data["daily"]["temperature_2m_max"]
min_data = data["daily"]["temperature_2m_min"]

for date, max, min in zip(time_data, max_data, min_data):

    avg_temp = (max + min) / 2
    print(
        f"* On {date} the max temperature was {max} and minimum temperature was {min}, average temperature being {avg_temp}"
    )
