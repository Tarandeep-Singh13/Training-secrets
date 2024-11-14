import os
import requests
API_KEY = os.getenv("CAT_API_KEY")
url = "https://api.thecatapi.com/v1/images/search?limit=10&breed_ids=beng"

headers = {
    "x-api-key": API_KEY
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for index, cat in enumerate(data, start=1):
        print(f"Cat {index} - URL: {cat['url']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
