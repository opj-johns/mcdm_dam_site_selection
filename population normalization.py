# Original data
data = [
    8338.00, 12700.00, 8419.00, 652292.00, 9641.00, 8214.00, 30025.00, 5295.00,
    5449.00, 16554.00, 18381.00, 1276.00, 20978.00, 7168.00, 6912.00, 1494413.00,
    1494413.00, 154064.00, 13256.00, 14638.00, 39114.00, 10417.00, 8164.00,
    26052.00, 7539, 46963, 7055, 21502, 12471
]

# Scaling range
new_min = 0
new_max = 50

# Min-max normalization
old_min = min(data)
old_max = max(data)

scaled_data = [
    round(new_min + (x - old_min) * (new_max - new_min) / (old_max - old_min), 2)
    for x in data
]

# Output scaled data

print(scaled_data)
