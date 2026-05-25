# PostgreSQL Integration

## Objective

Integrate PostgreSQL database with Flask backend services for persistent incident storage and operational event management.

---

# Why PostgreSQL Was Added

Initially, the platform only:
- monitored services
- generated logs
- triggered alerts

But incidents were not stored permanently.

PostgreSQL was added to provide:

- persistent incident storage
- structured operational records
- incident lifecycle tracking
- backend data persistence
- API-driven incident management

This transformed the project from:
```text
monitoring scripts
```

into:
```text
backend-driven incident response platform
```

---

# Architecture Flow

```text
Monitoring Scripts
        ↓
Incident Detection
        ↓
PostgreSQL Database
        ↓
Flask REST APIs
        ↓
JSON Incident Responses
```

---

# PostgreSQL Installation

Installed PostgreSQL server on Ubuntu EC2 instance.

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib -y
```

---

# PostgreSQL Service Verification

Verified PostgreSQL service status:

```bash
sudo systemctl status postgresql
```

Expected status:

```text
active (running)
```

---

# Database Creation

Created dedicated incident-response database.

```sql
CREATE DATABASE incident_response;
```

---

# Database User Creation

Created isolated application database user.

```sql
CREATE USER incident_admin WITH PASSWORD 'StrongPassword123';
```

---

# Permission Management

Granted database privileges to application user.

```sql
GRANT ALL PRIVILEGES ON DATABASE incident_response TO incident_admin;
```

---

# Incident Table Design

Created structured incident storage table.

```sql
CREATE TABLE incidents (
    id SERIAL PRIMARY KEY,
    incident_type VARCHAR(100),
    severity VARCHAR(50),
    status VARCHAR(50),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

# Table Purpose

| Column | Description |
|---|---|
| id | Unique incident identifier |
| incident_type | Incident category |
| severity | Incident severity level |
| status | Incident status |
| description | Incident details |
| created_at | Incident creation timestamp |

---

# Test Incident Insertion

Inserted sample incident record.

```sql
INSERT INTO incidents (
    incident_type,
    severity,
    status,
    description
)
VALUES (
    'Flask Service Failure',
    'high',
    'resolved',
    'Flask service restarted automatically'
);
```

---

# Data Verification

Verified incident records.

```sql
SELECT * FROM incidents;
```

---

# Flask Database Integration

Integrated Flask backend with PostgreSQL database using:

```text
psycopg2-binary
```

---

# Python Dependencies

Added PostgreSQL driver inside:

```text
requirements.txt
```

```txt
flask
psycopg2-binary
```

---

# Flask Database Configuration

```python
DB_CONFIG = {
    "host": "localhost",
    "database": "incident_response",
    "user": "incident_admin",
    "password": "StrongPassword123"
}
```

---

# Incident API Endpoint

Implemented incident retrieval API.

```python
@app.route("/incidents")
def incidents():
```

---

# API Responsibilities

The API:
- connects to PostgreSQL
- retrieves incident records
- formats JSON responses
- returns operational incident data

---

# Features Implemented

- PostgreSQL integration
- persistent incident storage
- Flask database connectivity
- REST API incident retrieval
- operational event persistence
- backend data management

---

# Concepts Learned

## Backend Engineering
- database integration
- SQL operations
- API-driven data access

## Infrastructure Operations
- PostgreSQL administration
- Linux database management
- service verification

## Incident Management
- persistent event tracking
- operational logging
- incident lifecycle management

## REST API Development
- JSON responses
- backend routing
- database-driven APIs

---

# Future Improvements

Planned enhancements:

- incident severity analytics
- authentication system
- incident dashboard UI
- Grafana visualization
- automated database backups
- incident filtering APIs
- real-time alert ingestion
- Dockerized PostgreSQL deployment

---

# Final Outcome

The platform evolved from:

```text
basic monitoring scripts
```

to:

```text
backend-driven incident response and operational monitoring platform
```
# API Testing

Test endpoint:

```bash
curl http://localhost/incidents
```

Expected JSON response:

```json
{
  "incidents": [
    {
      "id": 1,
      "incident_type": "Flask Service Failure",
      "severity": "high",
      "status": "resolved"
    }
  ]
}
```