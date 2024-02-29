import requests
import time
import csv
import concurrent.futures

# Define the URL of the PHP project to test
url = "http://192.168.33.10/index.php"  # Replace with your PHP project URL

# Define the number of concurrent requests
concurrent_requests = 10

# Define the number of iterations
iterations = 10

# Define the headers for CSV file
csv_headers = ['Iteration', 'Request Number', 'Response Time (s)']

# Open CSV file for writing
with open('stress_test_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

    # Perform stress testing
    for iteration in range(iterations):
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
            futures = []
            for i in range(concurrent_requests):
                futures.append(executor.submit(requests.get, url))

            for i, future in enumerate(concurrent.futures.as_completed(futures)):
                response_time = future.result().elapsed.total_seconds()
                writer.writerow([iteration+1, i+1, response_time])
