# Socket Programming Project

This repository contains Python socket programming examples. Each folder demonstrates different networking concepts, from building simple web servers and clients to querying atomic clocks.

---

## Overview

### 1. `client-and-server/`
**Purpose:**
- Demonstrates a basic HTTP-like server and client interaction using sockets.

**Scripts:**
- `webserver.py` — Runs a simple server that responds with a plain text message to any HTTP request.
- `webclient.py` — Sends an HTTP GET request to a specified host and port, prints the server's response.

**Usage:**
- Start the server (default port 28333):
  ```bash
  python client-and-server/webserver.py [port]
  ```
- Run the client (specify host and optional port):
  ```bash
  python client-and-server/webclient.py <host> [port]
  ```
  Example:
  ```bash
  python client-and-server/webclient.py localhost 28333
  ```

---

### 2. `serving-files/`
**Purpose:**
- Implements a simple web server that serves static `.txt` and `.html` files over HTTP.
- Includes a client to request specific files from the server.

**Scripts:**
- `webserver.py` — Serves files in response to HTTP GET requests on port 33490. Returns `404 Not Found` if the file does not exist.
- `webclient.py` — Requests a file from the server and prints the response.

**Sample Files:**
- `file1.txt` — Example text file.
- `file2.html` — Example HTML file.

**Usage:**
- Start the server (serves files from the current directory):
  ```bash
  python serving-files/webserver.py
  ```
- Run the client (request a file, e.g. `/file1.txt` or `/file2.html`):
  ```bash
  python serving-files/webclient.py /file1.txt
  python serving-files/webclient.py /file2.html
  ```

---

### 3. `atomic-time/`
**Purpose:**
- Connects to the National Institute of Standards and Technology (NIST) atomic clock server to fetch the number of seconds since January 1, 1900.
- Compares the atomic time with your system's time.

**Script:**
- `main.py` — Connects to `time.nist.gov` on port 37, retrieves the time, and prints the difference from your system clock.

**Usage:**
```bash
python atomic-time/main.py
```

---

## Requirements
- Python 3.x (no external dependencies required)

## Notes
- All scripts use only the Python standard library.
- For the file server, ensure you run the client and server from the `serving-files/` directory so the server can find the files.
- Ports are hardcoded except for `client-and-server/webserver.py`, which allows an optional port argument.

---

## License
This project is for educational purposes. 