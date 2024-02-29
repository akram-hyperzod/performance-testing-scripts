**Performance Testing Scripts**
This repository contains Python scripts for performing Load, Stress, and Reliability testing on a PHP project. The scripts interact with the PHP project via HTTP requests and measure various performance metrics.

**Contents**
1. Load Testing Script
2. Stress Testing Script
3. Reliability Testing Script
4. Usage
5. Dependencies
6. License

**Load Testing Script**
The load testing script sends a specified number of HTTP requests to the PHP project and measures the response time for each request. The results are saved in a CSV file named load_test_results.csv.

**Stress Testing Script**
The stress testing script simulates concurrent users by sending multiple HTTP requests simultaneously to the PHP project. It measures the response time for each request and saves the results in a CSV file named stress_test_results.csv.

**Reliability Testing Script**
The reliability testing script sends HTTP requests to the PHP project and records the HTTP status codes returned by the server. It measures the reliability of the server under normal load conditions and saves the results in a CSV file named reliability_test_results.csv.

**Usage**
Clone this repository to your local machine:

git clone https://github.com/your-username/performance-testing-scripts.git
Navigate to the repository directory:

cd performance-testing-scripts
Install the required dependencies (see Dependencies).

Execute the desired testing script using Python:


python load_test.py

python stress_test.py

python reliability_test.py
Dependencies
The scripts require the following dependencies:

Python 3.x
Requests library (install via pip install requests)
License
This project is licensed under the MIT License - see the LICENSE file for details.
