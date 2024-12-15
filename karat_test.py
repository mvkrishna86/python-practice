import requests

def get_content(url):
    # URL Validation
    res = requests.get(url)
    if res.status_code != 200:
        return ""
    return res.text

content = get_content("https://public.karat.io/content/test/test_log.txt")
if content == "":
    exit()

# 2021-05-07 00:26:37.210 Block 14.143.105.99

logs_list = []

for line in content.splitlines():
    log = line.split()
    log_dict = {}
    log_dict["date"] = log[0]
    log_dict["time"] = log[1]
    log_dict["status"] = log[2]
    log_dict["ip"] = log[3]
    logs_list.append(log_dict)

for log in logs_list:
    time = log["time"].split(":")[0]
    time = int(time)
    if time >=2 and log["status"] == "Block":
        print(log)



    