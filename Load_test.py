import requests
import time
import statistics
from concurrent.futures import ThreadPoolExecutor, as_completed

post_url = "http://18.171.9.138/chatbot/wakeb"
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
    start_time = time.time()
    try:
        response_post = requests.post(post_url, headers=post_headers, json=payload, verify=False, timeout=10)
        response_time = time.time() - start_time
        return {
            'status_code': response_post.status_code,
            'response_time': response_time,
            'text': response_post.text
        }
    except requests.exceptions.RequestException as e:
        response_time = time.time() - start_time
        return {
            'error': str(e),
            'response_time': response_time
        }

def main():
    num_requests = 100  # Number of total requests
    concurrent_requests = 10  # Number of parallel requests
    response_times = []
    status_codes = {}

    with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        
        for future in as_completed(futures):
            result = future.result()
            
            if 'error' in result:
                print(f"Request failed: {result['error']}")
            else:
                response_times.append(result['response_time'])
                status_code = result['status_code']
                status_codes[status_code] = status_codes.get(status_code, 0) + 1
                print(f"Status Code: {status_code}, Response Time: {result['response_time']:.2f} seconds")

    if response_times:
        print("\n--- Performance Summary ---")
        print(f"Total Requests: {num_requests}")
        print(f"Successful Requests: {sum(status_codes.values())}")
        print(f"Failed Requests: {num_requests - sum(status_codes.values())}")
        print(f"Minimum Response Time: {min(response_times):.2f} seconds")
        print(f"Maximum Response Time: {max(response_times):.2f} seconds")
        print(f"Average Response Time: {statistics.mean(response_times):.2f} seconds")
        print(f"Median Response Time: {statistics.median(response_times):.2f} seconds")
        print(f"Standard Deviation of Response Times: {statistics.stdev(response_times):.2f} seconds")
        print("\nStatus Code Distribution:")
        for code, count in status_codes.items():
            print(f"  {code}: {count} responses")

if __name__ == "__main__":
    main()
