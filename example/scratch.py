import requests

url = 'https://www.google.com/'

myHeaders = {'content-type':'html/text'}
response = requests.get(url, headers=myHeaders)
resoibse = requests.get(url, headers={'content-type': 'html/text'})

response.status_code # 200 is good
response.json()

### POST REQUEST ###
import requests 
url = "https://httpbin.org/post"
data = {
    "id": 1001, 
    "name": "alice",
    "passion": "coding"
}

response = requests.post(url, jason=data)

print("status Code", response.status_code)
print("JSON Resoponse", response.json())