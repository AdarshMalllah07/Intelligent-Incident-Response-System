# Centralized Logging & Incident Analysis

## Objective

Implement centralized logging and operational visibility for the Intelligent Incident Response System.

---

# Why Logging Is Important

Monitoring detects problems.

Logging explains:
- why problems happened
- what failed
- when failures occurred
- request patterns
- operational behavior

Without logs:
incident debugging becomes difficult.

---

# Logging Components

## Flask Application Logs

Tracks:
- incoming requests
- health checks
- application errors
- operational events

---

## Nginx Access Logs

Tracks:
- browser traffic
- scanners
- attack attempts
- HTTP requests

---

## CloudWatch Logs

Provides:
- centralized storage
- cloud-based log access
- historical analysis
- searchable logs

---

# Flask Logging Configuration

## Log Directory

```text
/var/log/flask-app/
```

---

## Log File

```text
/var/log/flask-app/app.log
```

---

# Application Logging Code

```python
logging.basicConfig(
    filename='/var/log/flask-app/app.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
```

---

# Flask Endpoints

## Home Endpoint

```text
/
```

Tracks incoming traffic.

---

## Health Endpoint

```text
/health
```

Used for monitoring and health validation.

---

## Error Endpoint

```text
/error
```

Simulates application failures for testing.

---

# Viewing Application Logs

```bash
cat /var/log/flask-app/app.log
```

---

# Viewing Nginx Logs

```bash
sudo tail -f /var/log/nginx/access.log
```

---

# CloudWatch Log Collection

CloudWatch Agent configured to collect:

- Flask logs
- Nginx access logs
- system metrics

---

# CloudWatch Log Groups

## Flask Logs

```text
flask-app-logs
```

---

## Nginx Logs

```text
nginx-access-logs
```

---

# Operational Benefits

Centralized logging improves:

- incident analysis
- troubleshooting
- observability
- infrastructure visibility
- operational debugging

---

# Concepts Learned

- centralized logging
- operational visibility
- application telemetry
- observability
- cloud log aggregation
- incident investigation