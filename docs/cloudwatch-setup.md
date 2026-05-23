# CloudWatch Monitoring Setup

## Objective

Configure AWS CloudWatch Agent to collect EC2 server metrics for monitoring and incident detection.

---

# Why Monitoring Is Important

Production systems must continuously expose health information.

Monitoring helps detect:
- resource exhaustion
- application failures
- abnormal behavior
- infrastructure degradation

This is foundational for incident response systems.

---

# CloudWatch Agent Installation

## Install Agent

```bash
sudo apt install amazon-cloudwatch-agent -y
```

If package unavailable:

```bash
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
```

```bash
sudo dpkg -i amazon-cloudwatch-agent.deb
```

---

# CloudWatch Agent Configuration

## Create Configuration File

```bash
sudo nano /opt/aws/amazon-cloudwatch-agent/bin/config.json
```

---

## Configuration

```json
{
  "metrics": {
    "metrics_collected": {
      "mem": {
        "measurement": [
          "mem_used_percent"
        ]
      },
      "disk": {
        "measurement": [
          "used_percent"
        ],
        "resources": [
          "/"
        ]
      }
    }
  }
}
```

---

# Start CloudWatch Agent

```bash
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
-a fetch-config \
-m ec2 \
-c file:/opt/aws/amazon-cloudwatch-agent/bin/config.json \
-s
```

---

# Verify Agent Status

```bash
sudo systemctl status amazon-cloudwatch-agent
```

Expected:

```text
active (running)
```

---

# Metrics Collected

| Metric | Purpose |
|---|---|
| mem_used_percent | Detect high memory usage |
| disk_used_percent | Detect disk exhaustion |

---

# Architecture Flow

```text
EC2 Server
   ↓
CloudWatch Agent
   ↓
AWS CloudWatch
   ↓
Metrics Dashboard
```

---

# Future Enhancements

Planned monitoring features:
- CPU alarms
- Memory alarms
- Disk alarms
- SNS notifications
- Auto-remediation
- Incident automation