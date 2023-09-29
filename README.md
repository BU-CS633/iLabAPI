# CS633 Team-2: iLabAPI

Welcome to the iLabAPI repository. This is a backend repository for the iLab platform. This guide will walk you through the process of cloning, setting up, and running the project on your local machine.
Project detail can be found in [this Google Docs](https://docs.google.com/document/d/1LrAqqTd58ldKJLBiHCrjrwJL641t1vtTooFNEX3d2c8/edit?usp=sharing)

Backend will be built using Python with the Django framework. All codebase will be stored in github: https://github.com/BU-CS633/iLabAPI. Details about installation can be found in the same link.
Deployment will be done automatically every time there's a push commit into the main branch. The api can be accessed from https://ilab-api.onrender.com/api.

**File structure:**
- `iLabAPI/iLabAPI` will contain all Django and app configuration.
- `iLabAPI/api` will contain all API and its functionality.

Developers feel free to create a new dedicated file to contain the logic, but please be aware to put it in accessible places so it can be easily imported if someone needs to reuse the same function.

## Prerequisites

Ensure you have the following installed:

- Python (Preferably 3.6 or newer)
- Pip (Python package installer)
- Virtual environment (optional, but recommended)
- PostgreSQL (Version 15)

## Development Workflow
Trunk based development will be used to allow smooth collaboration and faster feature release. The implementation is below:

1. Suppose you take a task from Pivotal Tracker, checkout from the main branch and create a new branch for your development.
```bash
Git checkout main
Git checkout -b <your_development_branch_name>
```
2. Do the code.
3. Push your development branch.
```bash
Git add .
Git commit -m "<your_commit_message>"
Git push origin <your_development_branch_name>
```
4. Create a pull request from your development branch into main.
Make sure it has no conflict.
5. Ask for a review.
6. If you need to change something, do steps 2 and 3, and then ask to review again.
7. Once the PR is approved, merge PR to the main branch to trigger the deployment process.

## Installation

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
Once the server is running, you can visit http://127.0.0.1:8000/api or http://127.0.0.1:8000/admin in your browser.