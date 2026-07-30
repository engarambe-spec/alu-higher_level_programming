# python-network_1

This project covers fetching internet resources from Python using
both the standard library (`urllib`) and the `requests` package:
making GET/POST requests, reading response headers and bodies,
handling HTTP errors, working with JSON, and using Basic Authentication
against the GitHub API.

## Learning Objectives

- How to fetch internet resources with the Python package urllib
- How to decode a urllib body response
- How to use the Python package requests
- How to make HTTP GET and POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements

- Every file starts with exactly `#!/usr/bin/python3`
- Code follows PEP 8 style
- Every file is executable and ends with a new line
- Every module is documented with a real explanatory docstring
- Dictionary values are accessed with `.get()`
- Scripts don't execute on import (`if __name__ == "__main__":`)

## Files

| File | Description |
|------|-------------|
| 0-hbtn_status.py | Fetches /status with urllib, prints the body |
| 1-hbtn_header.py | Prints the X-Request-Id header, via urllib |
| 2-post_email.py | POSTs an email param, via urllib |
| 3-error_code.py | Prints the body or `Error code: <code>`, via urllib |
| 4-hbtn_status.py | Fetches /status with requests, prints the body |
| 5-hbtn_header.py | Prints the X-Request-Id header, via requests |
| 6-post_email.py | POSTs an email param, via requests |
| 7-error_code.py | Prints the body or `Error code: <code>`, via requests |
| 8-json_api.py | Searches a user by letter, prints `[id] name` or errors |
| 10-my_github.py | Prints a GitHub user's id via Basic Authentication |

## Testing

Tasks 0-3 and 4-8 were verified against a local Flask server
replicating the container's routes (`/status`, `/post_email`,
`/status_401`, `/status_500`, `/search_user`), and every output
matched the spec exactly. Task 10 was verified against the real
GitHub API (`api.github.com`).

## Author

qshejantab-byte
