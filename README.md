# Agent Reporting Prototype

This is a Django-based backend project for analyzing historical system data for agents. It includes a RESTful API to generate reports summarizing software installed on an agent's system, with first and last seen dates, using PostgreSQL and Django ORM for data management.

## Project Overview

The project fulfills the requirements of an assignment to create a reporting feature that analyzes historical data for agents. Key features include:

- **Models**: `Agent`, `Software`, `SystemSnapshot`, and `SnapshotSoftware` to store agent data and software snapshots.
- **API Endpoint**: `/api/agents/{id}/report/` to aggregate software history (first and last seen dates) for a given agent.
- **Data Population**: A script to populate the database with historical data for two agents over 10 days.
- **Admin Panel**: Django admin interface to manage and view data.
- **Technologies**: Django 5.2.5, Django REST Framework, PostgreSQL, and `psycopg2-binary`.

## Prerequisites

- Python 3.8+
- PostgreSQL 12+ (with `psycopg2-binary` for database connectivity)
- Git (for cloning the repository)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/princebabou/Django_hdrm.git
   cd Django_hdrm
   ```

2. **Install Dependencies**:
   Create and activate a virtual environment, then install required packages:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set Up PostgreSQL**:
   - Ensure PostgreSQL is installed and running.
   - Create a database named `hdrm_project`:
     ```sql
     psql -U postgres
     CREATE DATABASE hdrm_project;
     GRANT ALL PRIVILEGES ON DATABASE hdrm_project TO postgres;
     ```
   - Verify database settings in `acc_project/settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'hdrm_project',
             'USER': 'postgres',
             'PASSWORD': 'your_password',  # Replace with your PostgreSQL password
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Populate the Database**:
   Run the data population script to create sample data (2 agents, 5 software entries, 20 snapshots):
   ```bash
   python manage.py shell
   from reports.populate_data import populate_data
   populate_data()
   ```

6. **Create a Superuser** (for admin panel access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Access the project at `http://localhost:8000`.

## Usage

- **Admin Panel**:
  - URL: `http://localhost:8000/admin/`
  - Log in with the superuser credentials to view and manage `Agent`, `Software`, `SystemSnapshot`, and `SnapshotSoftware` data.
  - Example: View `Agent_A` and `Agent_B` under `Reports > Agents`.

- **API Endpoint**:
  - URL: `http://localhost:8000/api/agents/{id}/report/`
  - Example: `http://localhost:8000/api/agents/1/report/`
  - Response (JSON):
    ```json
    {
        "agent": "Agent_A",
        "software_summary": [
            {
                "software": "Antivirus_X",
                "first_seen": "2025-08-11T21:19:12.307545Z",
                "last_seen": "2025-08-19T21:19:12.307545Z"
            },
            ...
        ]
    }
    ```
  - Use `curl` or a browser to test:
    ```bash
    curl http://localhost:8000/api/agents/1/report/
    ```

- **Database Inspection**:
  - Connect to PostgreSQL:
    ```bash
    psql -U postgres -d hdrm_project
    ```
  - View data:
    ```sql
    SELECT * FROM reports_agent;
    SELECT * FROM reports_snapshotsoftware LIMIT 5;
    ```

## Project Structure

- `acc_project/`: Project settings and main URL configuration.
- `reports/`: App containing models, views, URLs, and data population script.
  - `models.py`: Defines `Agent`, `Software`, `SystemSnapshot`, `SnapshotSoftware`.
  - `views.py`: Implements `/api/agents/{id}/report/` endpoint with Django ORM aggregation.
  - `urls.py`: Routes API requests.
  - `populate_data.py`: Populates database with sample data.
  - `admin.py`: Registers models for admin panel.
- `requirements.txt`: Lists dependencies (`django`, `djangorestframework`, `psycopg2-binary`).

## Challenges and Solutions

- **Switching from SQLite to PostgreSQL**:
  - Updated `settings.py` with PostgreSQL configuration.
  - Installed `psycopg2-binary` for database connectivity.
- **Empty Database Tables**:
  - Debugged `populate_data.py` to ensure data insertion.
  - Verified data with `psql` queries.
- **API Data Retrieval**:
  - Ensured correct ORM query using `Min` and `Max` for timestamp aggregation.
  - Validated agent IDs and relationships in `SnapshotSoftware`.
