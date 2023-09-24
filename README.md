# CS633 Team-2: iLabAPI

Welcome to the iLabAPI repository. This is a backend repository for the iLab platform. This guide will walk you through the process of cloning, setting up, and running the project on your local machine.

## Prerequisites

Ensure you have the following installed:

- Python (Preferably 3.6 or newer)
- Pip (Python package installer)
- Virtual environment (optional, but recommended)
- PostgreSQL (Version 15)

## Steps to Clone and Run

1. Clone the Repository
```bash
git clone https://github.com/BU-CS633/iLabAPI.git
cd iLabAPI
```

2. Set Up a Virtual Environment (Optional)
Using a virtual environment is recommended to avoid conflicts with other Python projects:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the Required Packages
```bash
pip install -r requirements.txt
```

4. Create `.env` file under the `iLabAPI` folder. Theres a `.env.example` file in that folder that you can modify the content according to your configuration and rename it to `.env`.


5. Apply Migrations
Before running the server for the first time, create a database called `ilab` (also use this value as `DB_NAME` in the `.env` file) and then apply migrations to set up your database schema:
```bash
python manage.py migrate
```

6. Run the Development Server
```bash
python manage.py runserver
```
Once the server is running, you can visit http://127.0.0.1:8000/ in your browser.