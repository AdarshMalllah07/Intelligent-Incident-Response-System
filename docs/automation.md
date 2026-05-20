# Automation & Auto Remediation

## Objective

Implement automatic incident detection and service recovery for Flask application failures.

---

# Why Auto Remediation Matters

Manual recovery introduces:
- downtime
- operational delays
- human dependency
- slower incident response

Auto-remediation reduces Mean Time To Recovery (MTTR).

---

# Health Check Workflow

```text
Health Check Request
        ↓
Validate HTTP Response
        ↓
Detect Failure
        ↓
Restart Flask Service
        ↓
Log Recovery Action
```

---

# Automation Script

## Script Location

```text
/home/ubuntu/automation/flask-health-check.sh
```

---

# Health Check Script

```bash
#!/bin/bash

APP_URL="http://127.0.0.1/health"
LOG_FILE="/home/ubuntu/automation/remediation.log"

HTTP_STATUS=$(curl -s -o /dev/null -w "%{http_code}" $APP_URL)

if [ "$HTTP_STATUS" -ne 200 ]; then
    echo "$(date) - Flask app unhealthy. Restarting service..." >> $LOG_FILE

    sudo systemctl restart flask-app

    echo "$(date) - Flask service restarted." >> $LOG_FILE
else
    echo "$(date) - Flask app healthy." >> $LOG_FILE
fi
```

---

# Script Permissions

```bash
chmod +x flask-health-check.sh
```

---

# Manual Script Execution

```bash
./flask-health-check.sh
```

---

# Flask Health Endpoint

```text
http://127.0.0.1/health
```

Expected Response:

```json
{
  "status": "healthy"
}
```

---

# Incident Simulation

## Simulate Flask Failure

```bash
sudo systemctl stop flask-app
```

---

# Recovery Validation

Run:

```bash
./flask-health-check.sh
```

Verify:

```bash
sudo systemctl status flask-app
```

Expected:

```text
active (running)
```

---

# Recovery Logs

```bash
cat remediation.log
```

---

# Concepts Learned

- health checks
- self-healing systems
- operational automation
- Linux service recovery
- incident remediation
- infrastructure reliability