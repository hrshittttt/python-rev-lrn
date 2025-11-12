import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

today = datetime.now()
week_ago = today - timedelta(days=7)

end_date = today.strftime("%Y-%m-%d")
start_date = week_ago.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
data = requests.get(url)

response = data.json()

daily_data = response["daily"]

df = pd.DataFrame(
    {
        "time_data": daily_data["time"],
        "max_temp_data": daily_data["temperature_2m_max"],
        "min_temp_data": daily_data["temperature_2m_min"],
    }
)

df["time_data"] = pd.to_datetime(df["time_data"])

plt.figure(figsize=(10, 6))
plt.plot(df["time_data"], df["max_temp_data"], label="Max Temp.")
plt.plot(df["time_data"], df["min_temp_data"], label="Max Temp.")

plt.xlabel("Date")
plt.ylabel("Temperature in °C")
plt.title("Paris weather in last 7 days")
plt.legend()

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("weather_chart.png")
plt.show()
