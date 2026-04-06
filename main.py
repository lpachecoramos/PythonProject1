rain_total = 0.0
wind_total = 0.0
count = 0

while True:
    data = input().split()

    rain = float(data[0])

    # Sentinel value
    if rain == -1.0:
        break

    wind = float(data[1])

    rain_total += rain
    wind_total += wind
    count += 1

# average
avg_rain = rain_total / count
avg_wind = wind_total / count

# Calculate weather severity
severity = (avg_rain * 10) + avg_wind

# outputs
print(f"The average rain is {avg_rain:.1f} inches")
print(f"The average wind is {avg_wind:.1f} mph")
print(f"The weather severity for these {count} readings is:     {severity:.1f}")