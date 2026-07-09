# Build your first API endpoint

**Assignment Code:** BE-01  
**Track:** Backend AI Engineering  
**Program:** FlyRank AI Internship

## Overview

This is the Week 1 setup assignment. It features a minimal backend built with **FastAPI** to demonstrate the fundamental request → response loop. The server exposes two simple JSON endpoints and is designed to be lightweight and easily reproducible.

## Tech Stack

- **Language:** Python 3
- **Framework:** FastAPI
- **Server:** Uvicorn (ASGI)

## How to Run Locally

1. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # For Windows (Git Bash)
   # source venv/bin/activate    # For Mac/Linux
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the local development server:
   ```bash
   uvicorn main:app --reload
   ```

The server will run at http://127.0.0.1:8000

## API Endpoints

1. **Root Endpoint**
   - **URL:** `/`
   - **Method:** GET
   - **Description:** Returns a welcome message and assignment status.
   - **cURL Test:** `curl http://127.0.0.1:8000/`

2. **Intern Endpoint**
   - **URL:** `/intern`
   - **Method:** GET
   - **Description:** Returns details about the intern's track and current learning phase.
   - **cURL Test:** `curl http://127.0.0.1:8000/intern`

## Project Structure

- `main.py`: Contains the FastAPI application and endpoint definitions.
- `requirements.txt`: Pinned Python dependencies.
- `.gitignore`: Excludes virtual environments and cache files from version control.
- `README.md`: Project documentation and setup instructions.
