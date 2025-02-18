# Performance Testing Scripts in Python

## Overview
This repository contains Python scripts for conducting performance testing without relying on any external tools or frameworks. The scripts use built-in Python libraries and efficient concurrency models to assess the responsiveness, reliability, and scalability of APIs or web services.

## Importance of This Project
Effective performance testing is essential for ensuring the stability and efficiency of applications under different levels of user load. The scripts in this repository allow developers and testers to:
- Measure response times and latency
- Analyze server behavior under concurrent requests
- Identify performance bottlenecks
- Evaluate the system's ability to handle multiple users simultaneously

By leveraging multi-threading and asynchronous programming, these scripts provide a simple yet powerful approach to performance testing.

## Scripts Description

### 1. `Load_test.py`
This script simulates multiple concurrent users sending HTTP POST requests to a given API endpoint and records performance metrics.

**Key Features:**
- Uses `ThreadPoolExecutor` for concurrency
- Sends a defined number of requests in parallel
- Records response times and HTTP status codes
- Computes statistical metrics such as min, max, average, and standard deviation of response times
- Provides a performance summary at the end

**Usage:**
```sh
python Load_test.py
```

---

### 2. `multiuser.py`
This script tests the API's ability to handle a high number of simultaneous requests, mimicking real-world traffic conditions.

**Key Features:**
- Uses `ThreadPoolExecutor` to launch a large number of parallel requests
- Captures response status codes and response texts
- Reports failed requests and errors

**Usage:**
```sh
python multiuser.py
```

---

### 3. `sequence_requests.py`
This script performs sequential API requests using asynchronous programming to optimize performance.

**Key Features:**
- Uses `aiohttp` and `asyncio` for efficient non-blocking HTTP requests
- Sends multiple requests in a sequential manner
- Captures response status codes and texts
- Handles errors gracefully

**Usage:**
```sh
python sequence_requests.py
```

## Dependencies
This project uses standard Python libraries except for `aiohttp` (used in `sequence_requests.py`). Install it using:
```sh
pip install aiohttp
```

## How to Use
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo-name.git
   cd your-repo-name
   ```
2. Run any script based on your testing requirements.
3. Review the output and analyze the performance results.

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests to enhance the scripts.

## License
This project is open-source and available under the MIT License.

