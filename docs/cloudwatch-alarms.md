# CloudWatch Alarms & Incident Detection

## Objective

Configure CloudWatch alarms to automatically detect abnormal infrastructure behavior.

---

# Alarm Workflow

```text
EC2 Metrics
     ↓
CloudWatch
     ↓
Alarm Evaluation
     ↓
SNS Notification
```

---

# Alarm Configured

## High CPU Alarm

### Metric
```text
CPUUtilization
```

### Threshold
```text
Greater than 60%
```

### Evaluation
```text
1 minute
```

---

# SNS Notifications

Configured SNS topic for incident alert notifications.

## Topic Name

```text
incident-alerts
```

---

# Incident Simulation

## Generate CPU Stress

```bash
stress --cpu 2 --timeout 300
```

---

# Expected Alarm Behavior

- CPU utilization increases
- CloudWatch alarm enters ALARM state
- SNS notification triggered

---

# Monitoring Concepts Learned

- metrics collection
- threshold monitoring
- incident detection
- infrastructure observability
- cloud alerting
- operational telemetry