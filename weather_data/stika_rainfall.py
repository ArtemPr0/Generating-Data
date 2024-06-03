from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('C:\\Users\\prokart\\Desktop\\Python\\generating_data_project\\weather_data\\sitka_weather_2021_simple.csv')
lines = path.read_text(encoding='utf-8').splitlines()


reader = csv.reader(lines)
header_row = next(reader)

# Extract dates. and high and low temperatures.
dates, rains = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    prcp = int(row[5])
    dates.append(current_date)
    rains.append(prcp)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(dates, rains, color='skyblue')
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Precipitation in Stika, 2021")
ax.set_xlabel("Date")
fig.autofmt_xdate()
ax.set_ylabel("PRCP (inches)")
ax.tick_params(axis='x', rotation=45)

# Remove the top and right axes.
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.show()

