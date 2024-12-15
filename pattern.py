
########################################
# traffic_data_sorted = sorted(traffic_data, key=lambda x: x[0])
########################################
# def get_timestamp(item):
#     return item[0]

# traffic_data.sort(key=get_timestamp)

def find_anamoly(data):
    prev_count = -1
    
    for ins in data:
        if prev_count == -1:
            prev_count = ins[1]
            break
        curr_count = ins[1]
        diff = curr_count - prev_count
        if diff > 15:
            print(f"Anamoly detected at {ins[0]}")

data = [
    [1702598400, 120],  # Timestamp in seconds since epoch and request count
    [1702602000, 85],
    [1702605600, 90],
    [1702609200, 110],
    [1702612800, 150],
    [1702616400, 95],
    [1702620000, 200],
    [1702623600, 175],
    [1702627200, 130],
]

# Explanation:
# - `1702598400` corresponds to "2024-12-15 00:00:00 UTC"
# - Use `datetime.datetime.utcfromtimestamp(timestamp)` to convert back to a readable format if needed.
