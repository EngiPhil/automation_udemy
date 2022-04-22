import requests
import bs4

# Sending request with URL
base_url = 'http://www.theTestingWorld.com'

response = requests.get(base_url)
"""
f = open('C:/Users/FilipV/Filip/PyCharm/Automation1/OutputFiles/result.txt', 'wb')
# How exactly works iter_content?
for data in response.iter_content(10000):
    f.write(data)
f.close()
"""

parsed_data = bs4.BeautifulSoup(response.text)

all_links = parsed_data.select('a')
# print(len(all_links))

for link in all_links:
    # print(link.getText())
    # print(link.get('href'))
    # print(link.get('title'))
    print(link.attrs)

