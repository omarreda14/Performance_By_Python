import requests

post_url = "http://18.130.9.168/chatbot/sdaia"
post_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Connection": "keep-alive",
    "Content-Length": "20",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "18.130.9.168",
    "Origin": "http://mujib-plus.wakeb.tech",
    "Referer": "http://mujib-plus.wakeb.tech/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

payload = {
    "query": "اهلا"
}

try:
    response_post = requests.post(post_url, headers=post_headers, json=payload, verify=False)
    print("\nPOST Response:")
    print(f"Status Code: {response_post.status_code}")

    try:
        json_response = response_post.json()
        print("JSON Response:", json_response)
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON, raw response text:")
        print(response_post.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
