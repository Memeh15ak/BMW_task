# BMW QR-Based Part Traceability System

A backend system to scan and store genuine BMW part details via QR code, capturing location and timestamp, and secured with JWT authorization for service centers.

## Features
- POST /scan-part to log part scans
- GET /part/{part_id} to view history (requires JWT)

## Tech Stack
- FastAPI
- MongoDB
- JWT (python-jose)
- Geolocation support

## Run Instructions
1. Install deps: `pip install -r requirements.txt`
2. Start server: `uvicorn main:app --reload`

## ✅ Sample Scan Saved via Swagger

![Fast api Success](Part1/media/Screenshot%202025-07-26%20125217.png)

## ✅ Scan Visible in MongoDB Compass
![MongoDB Compass](Part1/media/Screenshot%202025-07-26%20125332.png)

