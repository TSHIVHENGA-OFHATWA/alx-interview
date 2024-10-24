# Log Parsing Project

## Description
This project involves creating a Python script that reads input logs line by line, parses the information, and computes specific metrics. The script processes logs in a specified format and outputs the total file size and counts of HTTP status codes at regular intervals (every 10 lines or when interrupted by `CTRL + C`).

## Input Format
Each log entry has the following format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

- **IP Address**: IPv4 address of the client.
- **Date**: Date and time when the request was made.
- **GET request**: Specific GET request format.
- **Status code**: HTTP status code (200, 301, 400, 401, 403, 404, 405, 500).
- **File size**: Size of the file requested.

If a log entry does not conform to this format, it is ignored.

## Output
After every 10 lines or upon keyboard interruption (CTRL + C), the script prints:
1. **Total file size**: The sum of the file sizes from all valid lines.
2. **Number of lines by status code**: Counts of each HTTP status code in ascending order.

## Files
- `0-stats.py`: The main Python script that performs log parsing and outputs statistics.
- `0-generator.py`: A helper script that generates random log entries to simulate input for testing purposes.

## How to Run
1. Make sure you have Python 3 installed on your machine.
2. Run the generator script and pipe its output to the log parsing script:
    ```bash
    ./0-generator.py | ./0-stats.py
    ```
3. The statistics will be printed after every 10 lines or when interrupted with `CTRL + C`.

## Author
**Ofhatwa Tshivhenga**
