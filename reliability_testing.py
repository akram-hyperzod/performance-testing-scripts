import requests
import csv

# Define the URL of the PHP project to test
url = "http://192.168.33.10/index.php"  # Replace with your PHP project URL

# Define the number of requests to send
num_requests = 100

# Define the headers for CSV file
csv_headers = ['Request Number', 'HTTP Status Code']

# Open CSV file for writing
with open('reliability_test_results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)

    # Perform reliability testing
    for i in range(num_requests):
        response = requests.get(url)
        http_status_code = response.status_code
        writer.writerow([i+1, http_status_code])
