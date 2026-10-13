# Web App Security Lab: Broken Access Control (IDOR)

A demonstration of Insecure Direct Object Reference (IDOR) vulnerabilities and server-side authorization enforcement built with Python and Flask.

## Vulnerability Demonstrated
The `/vulnerable/student` endpoint blindly processes student IDs directly from URL parameters (`?id=102`) without ownership verification, allowing an authenticated student to read other students' private grades and records.

## The Mitigation
The `/secure/student` endpoint validates that the requester's session matches the targeted record ID, blocking unauthorized access with an HTTP 403 Forbidden response.

## How to Run
1. Install dependencies: `pip3 install flask`
2. Start server: `python3 app.py`
3. Open browser: `http://127.0.0.1:5000`
