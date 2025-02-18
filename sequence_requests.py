import asyncio
import aiohttp

post_url = ["URL"]
post_headers = {"Header"}

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
