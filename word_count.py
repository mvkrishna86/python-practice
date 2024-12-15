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

word_counts = {}

for word in content.split():
    if word in word_counts:
        c = word_counts[word]
        word_counts[word] = c + 1
    else:
        word_counts[word] = 1

count_dict = {}
for key, value in word_counts.items():
    if value in count_dict:
        count_dict[value].append(key)
    else:
        count_dict[value] = list(key)
i = 0
for key, value in sorted(count_dict.items(),reverse=True):
    if i < 5:
        print(key, value)
    else: 
        break
    i = i + 1


