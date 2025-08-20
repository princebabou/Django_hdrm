# Release v1.0.0 - Agent Reporting Prototype

This release delivers a fully functional Django-based backend for analyzing historical agent data, meeting the requirements of the assignment to create a reporting feature using PostgreSQL and Django ORM.

## Features

- **Models**:
  - `Agent`: Stores agent information (e.g., `Agent_A`, `Agent_B`).
  - `Software`: Stores software names (e.g., `Antivirus_X`, `Browser_Y`).
  - `SystemSnapshot`: Links agents to timestamps for system snapshots.
  - `SnapshotSoftware`: Many-to-many relationship between snapshots and software.
- **API Endpoint**:
  - `/api/agents/{id}/report/`: Aggregates software history for an agent, showing each software’s name, first seen, and last seen dates using Django ORM’s `Min` and `Max`.
  - Example response:
    ```json
    {
        "agent": "Agent_A",
        "software_summary": [
            {"software": "Antivirus_X", "first_seen": "2025-08-11T21:19:12.307545Z", "last_seen": "2025-08-19T21:19:12.307545Z"},
            ...
        ]
    }
    ```
- **Data Population**:
  - `populate_data.py`: Creates 2 agents, 5 software entries, 20 snapshots (2 agents × 10 days), and 40–80 `SnapshotSoftware` entries with random software assignments.
- **Admin Panel**:
  - Registered models (`Agent`, `Software`, `SystemSnapshot`, `SnapshotSoftware`) for data management at `http://localhost:8000/admin/`.
- **Technologies**:
  - Django 5.2.5, Django REST Framework, PostgreSQL, `psycopg2-binary`.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/princebabou/Django_hdrm.git
   cd acc-project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure PostgreSQL database `hdrm_project` and update `acc_project/settings.py`.
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Populate data:
   ```bash
   python manage.py shell
   from reports.populate_data import populate_data
   populate_data()
   ```
6. Start the server:
   ```bash
   python manage.py runserver
   ```

## Challenges and Solutions

- **Switching from SQLite to PostgreSQL**:
  - Configured `settings.py` with PostgreSQL settings and installed `psycopg2-binary`.
  - Ensured database connectivity with `psql -U postgres -d hdrm_project`.
- **Empty Database Tables**:
  - Debugged `populate_data.py` to ensure successful data insertion.
  - Verified data with SQL queries (e.g., `SELECT * FROM reports_agent;`).
- **API Functionality**:
  - Validated ORM query in `views.py` to correctly aggregate timestamps.
  - Tested endpoint with `curl http://localhost:8000/api/agents/1/report/`.

## Installation Notes

- Ensure PostgreSQL is running and the `hdrm_project` database is created.
- Update `settings.py` with your PostgreSQL password.
- Dependencies are listed in `requirements.txt`.

## Future Improvements

- Add authentication to secure the API endpoint.
- Implement pagination for large datasets.
- Add frontend interface for visualizing reports.