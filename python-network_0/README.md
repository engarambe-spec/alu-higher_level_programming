# python-network_0

This project covers the fundamentals of HTTP and how to interact with
web servers using cURL from the command line: request bodies,
response status codes, HTTP methods (GET, DELETE, OPTIONS), custom
headers, and POST parameters.

## Learning Objectives

- What a URL is, and how to read one (scheme, domain, sub-domain,
  port, resource path, query string)
- What HTTP is, and the request/response cycle
- What HTTP headers and the message body are
- What HTTP request methods and response status codes are
- What an HTTP Cookie is
- How to make requests with cURL
- What happens when you type google.com in your browser

## Requirements

- All scripts are exactly 3 lines long (`wc -l file` prints 3)
- Every file starts with exactly `#!/bin/bash`
- The second line is a comment explaining what the script does
- Every `curl` call uses `-s` (silent mode)
- Every file ends with a new line and is executable

## Files

| File | Description |
|------|-------------|
| 0-body_size.sh | Displays the size (bytes) of a URL's response body |
| 1-body.sh | Displays the response body, only for a 200 status |
| 2-delete.sh | Sends a DELETE request and displays the response body |
| 3-methods.sh | Displays all HTTP methods a server accepts for a URL |
| 4-header.sh | Sends a GET with a custom X-HolbertonSchool-User-Id header |
| 5-post_params.sh | Sends a POST with email and subject parameters |

## Testing

Each script was tested end-to-end against a local Flask server that
replicates the routes described in the project spec (root, and
`route_1` through `route_6`), and every output matched the expected
result exactly.

To test against the provided container's web server on port 5000:
