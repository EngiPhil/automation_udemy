import requests
import bs4

# Sending request with URL
base_url = 'http://www.theTestingWorld.com'

response = requests.get(base_url)
print(response.text)
print(response.status_code)

f = open('C:/Users/FilipV/Filip/PyCharm/Automation1/OutputFiles/result.txt', 'wb')

# How exactly works iter_content?
for data in response.iter_content(10000):
    f.write(data)

f.close()
