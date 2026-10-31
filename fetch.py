import requests

url = "https://testx3roxr.vercel.app/"

try:
    response = requests.get(url, timeout=30)

    print("URL:", url)
    print("Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("\nResponse Body:")
    print(response.text)

except requests.exceptions.RequestException as e:
    print("Request failed:", e)
