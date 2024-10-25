0x03. Log Parsing
Overview
This project, "0x03. Log Parsing," focuses on parsing and processing log data in real-time using Python. The goal is to read data from the standard input, parse it according to a specific format, and calculate summary metrics such as file size and the number of occurrences of different HTTP status codes. The script is designed to handle data streams efficiently and produce metrics after every 10 lines or when a keyboard interruption (CTRL + C) occurs.

Requirements
All scripts must be written in Python 3 (version 3.4.3).
The code must comply with PEP 8 style guidelines (version 1.7.x).
Files must be executable and end with a new line.
The project will run on Ubuntu 20.04 LTS.
Learning Objectives
By completing this project, you will enhance your knowledge of:

File I/O: Reading from sys.stdin line by line.
Signal Handling: Handling keyboard interruptions using Python’s signal handling mechanisms.
Data Processing: Parsing input data and aggregating information to compute metrics.
Dictionaries in Python: Counting occurrences of status codes and calculating the total file size using Python dictionaries.
Regular Expressions: Validating and parsing log formats using regular expressions.
Exception Handling: Writing robust code that handles exceptions gracefully during file reading and data processing.
Input Format
The log entries follow this format:

php
Copy code
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
<IP Address>: IP address of the client making the request.
<date>: Date and time of the request.
<status code>: HTTP status code returned by the server.
<file size>: Size of the file in bytes.
If the input format does not match the expected format, the line will be skipped.

Output
The script will output two metrics after every 10 lines of input or when a keyboard interruption occurs:

Total file size: The cumulative file size from all parsed log entries.
Number of lines by status code: A count of each valid HTTP status code (200, 301, 400, 401, 403, 404, 405, 500).
Example Output
yaml
Copy code
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
Only status codes that appear will be printed, and they will be displayed in ascending order.

File Structure
0-stats.py: The script that reads logs from stdin, parses the data, computes metrics, and prints the results.
0-generator.py: A script that generates sample log entries for testing purposes.
How to Run
1. Running the Log Parsing Script
To run the log parsing script, you can provide log entries via stdin. You can test it using the provided 0-generator.py script, which generates random log entries.

bash
Copy code
./0-generator.py | ./0-stats.py
2. Handling Keyboard Interruption
To simulate real-time log parsing, you can press CTRL + C to interrupt the process. The script will then print the metrics up to the point of interruption.

Example Usage
bash
Copy code
alexa@ubuntu:~/0x03-log_parsing$ ./0-generator.py | ./0-stats.py
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Concepts Covered
File I/O in Python: Reading data from sys.stdin.
Signal Handling: Using Python to handle keyboard interruptions (CTRL + C).
Data Processing: Efficiently parsing input strings to extract the necessary data.
Dictionaries: Storing status code counts and accumulating file sizes.
Exception Handling: Catching errors during parsing and input handling.
Regular Expressions: Optionally using regex to validate log formats (though simple string operations may suffice).
Resources
Python Input and Output
Python Signal Handling
Python Regular Expressions
Python Dictionaries
Python Exceptions
Author
Project developed as part of the ALX Software Engineering curriculum.

License
This project is licensed under the MIT License.
