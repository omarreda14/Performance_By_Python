import requests

post_url = ["URL"]
post_headers = {"Header"}

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
