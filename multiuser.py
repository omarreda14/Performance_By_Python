import requests
import time

from concurrent.futures import ThreadPoolExecutor, as_completed

post_url = "http://18.171.9.138/chatbot/sdaia"
post_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "18.171.9.138",
    "Origin": "http://mujib-plus.wakeb.tech",
    "Referer": "http://mujib-plus.wakeb.tech/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
}

payload = {
    "query": "hello"
}

def send_request():
    try:
        response_post = requests.post(post_url, headers=post_headers, json=payload, verify=False)
        return {
            'status_code': response_post.status_code,
            'text': response_post.text
        }
    except requests.exceptions.RequestException as e:
        return {
            'error': str(e)
        }

def main():
    num_requests = 1000  # Number of parallel requests
    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        
        for future in as_completed(futures):
            result = future.result()

            if 'error' in result:
                print(f"Request failed: {result['error']}")
            else:
                print(f"Status Code: {result['status_code']}")
                print("Response Text:", result['text'])

if __name__ == "__main__":
    main()
