import requests

with open('/Users/igumnyash/Downloads/dataset_3378_2.txt') as link:
    url = link.readline().strip()
print(url)

file = requests.get(url)
print(len(file.text.splitlines()))
