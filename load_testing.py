import requests
import time
import csv

# Define the URL of the PHP project to test
url = "http://192.168.33.10/index.php"  # Replace with your PHP project URL

# Define the number of requests to send
num_requests = 100

# Define the headers for CSV file
csv_headers = ['Request Number', 'Response Time (s)']

# Open CSV file for writing
with open('load_test_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

    # Perform load testing
    for i in range(num_requests):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        response_time = end_time - start_time
        writer.writerow([i+1, response_time])
