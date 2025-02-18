import asyncio
import aiohttp

post_url = "http://18.130.9.168/chatbot/dga"
post_headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9,ar;q=0.8",
    "Connection": "keep-alive",
    "Content-Type": "application/json;charset=UTF-8",
    "Host": "18.130.9.168",
    "Origin": "http://mujib-plus.wakeb.tech",
    "Referer": "http://mujib-plus.wakeb.tech/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

payload = {
    "query": "اهلا"
}

async def send_request(session):
    try:
        async with session.post(post_url, headers=post_headers, json=payload) as response:
            status_code = response.status
            text = await response.text()
            return {
                'status_code': status_code,
                'text': text
            }
    except Exception as e:
        return {
            'error': str(e)
        }

async def main():
    num_requests = 10  # Number of sequential requests
    async with aiohttp.ClientSession() as session:
        for _ in range(num_requests):
            result = await send_request(session)
            if 'error' in result:
                print(f"Request failed: {result['error']}")
            else:
                print(f"Status Code: {result['status_code']}")
                print("Response Text:", result['text'])

if __name__ == "__main__":
    asyncio.run(main())
