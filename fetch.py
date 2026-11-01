import requests

base_url = "https://testx3roxr.vercel.app/"

urls = [
    base_url,
    base_url + "hello"
]

for url in urls:
    print("\n" + "=" * 80)
    print("Fetching URL:", url)

    try:
        response = requests.get(url, timeout=30)

        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("\nResponse Body:")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
