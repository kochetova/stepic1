import requests


with open('/Users/igumnyash/Downloads/dataset_3378_3.txt') as link:
    url = link.readline().strip()
print(url)

while requests.get(url).text.split()[0] != 'We':
    url = 'https://stepic.org/media/attachments/course67/3.6.3/' + requests.get(url).text
    print(url)

print(requests.get(url).text)
