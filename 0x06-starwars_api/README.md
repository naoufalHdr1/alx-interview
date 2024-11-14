# 0x06. Star Wars API

## Description

This project involves creating a script in JavaScript to fetch and display information about characters from Star Wars movies using the Star Wars API. Given a movie ID, the script will make an HTTP request to retrieve character data and display each character’s name in the correct order based on the API response.

The project demonstrates key concepts in JavaScript related to web programming, asynchronous API interactions, and handling HTTP requests.

## Concepts and Skills Required

### Key Concepts:

- **HTTP Requests in JavaScript:** Fetch data from an API using the request module or alternatives.
- **Working with APIs:** Use RESTful APIs, parse JSON data, and handle API responses.
- **Asynchronous Programming:** Manage asynchronous operations with callbacks, promises, and async/await.
- **Command Line Arguments in Node.js:** Access command-line arguments using process.argv.
- **Array Manipulation:** Iterate over arrays and manipulate data for output formatting.

## Getting Started

### Prerequisites

1. Node.js:
- Install Node.js 10.x using:
```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

2. Install `semistandard`:
- Install the `semistandard` linter globally:
```bash
sudo npm install semistandard --global
```

3. Install `request` module:
Install the `request` module globally:
```bash
sudo npm install request --global
export NODE_PATH=/usr/lib/node_modules
```

### Usage

Run the script as follows:
```bash
./0-starwars_characters.js <Movie_ID>
```

- **Movie_ID**: The ID of the Star Wars movie to fetch characters from.
- Example:
```bash
./0-starwars_characters.js 3
```

### Task

0. Star Wars Characters

Write a script that prints all characters of a Star Wars movie:
- The first positional argument passed is the Movie ID (e.g., `3` for "Return of the Jedi").
- Display each character's name on a new line, in the order they appear in the `/films/` endpoint's `characters` list.
- Use the Star Wars API (`https://swapi-api.alx-tools.com/`).
- Use the `request` module to make HTTP requests.

### Example Output:

For a movie ID of `3`, the output would list each character by name, as shown below:
```python
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```

### Implementation Details

- The script uses the **Star Wars API** (`https://swapi-api.alx-tools.com/`) to retrieve data.
- It processes JSON data and displays each character name in the specified order as per the API’s `characters` list.

### Files

- **0-starwars_characters.js**: The main script to fetch and print characters based on a given movie ID.

### Example Command
```bash
alexa@ubuntu:~/0x06$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
...
```
