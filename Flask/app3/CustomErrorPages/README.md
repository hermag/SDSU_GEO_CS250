# Flask Custom Error Pages Demo

This project demonstrates three different types of custom error pages in Flask:
1. 404 - Page Not Found
2. 500 - Internal Server Error
3. 403 - Forbidden

## Setup

1. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask application:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Click on the different buttons to see the custom error pages in action.

## Features

- Custom styled error pages with consistent design
- Error details shown for 500 errors in development mode
- Responsive design that works on all devices
- Easy navigation back to the home page 