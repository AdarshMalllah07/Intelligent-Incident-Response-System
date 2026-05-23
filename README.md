Intelligent-Incident-Response-System
## Current Progress

### Infrastructure Setup Completed
- AWS EC2 Ubuntu server deployed
- SSH access configured using PEM key
- Python virtual environment configured
- Flask application deployed
- Public access configured on port 5000
- Nginx installed on server

---

## Flask Endpoints

| Endpoint | Description |
|---|---|
| / | Main application endpoint |
| /health | Health check endpoint |

---

## Current Architecture

```text
Internet
   ↓
AWS EC2 Ubuntu Server
   ↓
Flask Application
```

---

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Python
- Flask
- Nginx
- SSH
- Git & GitHub

## Monitoring Setup

### CloudWatch Agent
Installed AWS CloudWatch Agent on EC2 instance to collect:

- Memory usage metrics
- Disk usage metrics
- System telemetry

---

## Current Production Architecture

```text
Internet
   ↓
Nginx Reverse Proxy
   ↓
Flask Application Service
   ↓
Ubuntu EC2 Server
   ↓
CloudWatch Agent
   ↓
AWS CloudWatch
```

---

## Production Features Implemented

- Flask running as systemd service
- Automatic service restart
- Reverse proxy architecture using Nginx
- Internal application isolation
- Cloud monitoring integration
- Linux service management
- Public web hosting

---

## Monitoring Goals

The monitoring system will later detect:

- High CPU usage
- High memory usage
- Disk exhaustion
- Flask service failures
- Nginx failures
- Server health degradation   

## Incident Detection & Auto Remediation

### Monitoring Features
- AWS CloudWatch monitoring integration
- Memory usage collection
- Disk usage collection
- CPU utilization monitoring
- CloudWatch alarm configuration
- SNS alert notifications

---

## Automation Features

### Flask Health Monitoring
Implemented automated Flask health-check system.

The automation:
- validates application health
- detects service failures
- automatically restarts Flask service
- logs remediation activity

---

## Self-Healing Workflow

```text
Health Check
      ↓
Failure Detection
      ↓
Automatic Service Restart
      ↓
Recovery Logging
```

---

## Operational Automation Script

### Health Check Endpoint

```text
/health
```

### Health Check Script

```bash
./flask-health-check.sh
```

---

## Current System Architecture

```text
Internet
   ↓
Nginx Reverse Proxy
   ↓
Flask Application Service
   ↓
Ubuntu EC2 Server
   ↓
CloudWatch Agent
   ↓
CloudWatch Monitoring
   ↓
CloudWatch Alarm
   ↓
SNS Notifications
   ↓
Automation Scripts

## Centralized Logging & Incident Analysis

### Logging Features Implemented

- Flask application logging
- Nginx access logging
- CloudWatch centralized log collection
- Application error simulation
- Operational event tracking

---

## Log Sources

| Source | Purpose |
|---|---|
| Flask Application Logs | Track application activity and errors |
| Nginx Access Logs | Track incoming traffic and scanners |
| CloudWatch Logs | Centralized cloud log storage |

---

## Flask Logging Features

The Flask application now records:

- incoming requests
- health check requests
- simulated errors
- operational activity

---

## Incident Analysis Features

The system now supports:

- application troubleshooting
- traffic analysis
- scanner detection
- operational debugging
- centralized observability

---

## Current Observability Architecture

```text
Internet
   ↓
Nginx Reverse Proxy
   ↓
Flask Application Service
   ↓
Application Logs
   ↓
CloudWatch Agent
   ↓
CloudWatch Logs

```
```
## Security Monitoring & Intrusion Detection

### Security Features Implemented

- Nginx traffic monitoring
- Suspicious request detection
- Attack pattern scanning
- Security incident logging
- Basic intrusion detection automation

---

## Threat Detection Capabilities

The system currently detects:

- phpunit vulnerability scans
- WordPress probing attempts
- xmlrpc attack attempts
- suspicious vendor scans
- CGI exploit scanning

---

## Security Monitoring Workflow

```text
Internet Traffic
      ↓
Nginx Access Logs
      ↓
Security Detection Scripts
      ↓
Security Incident Logs
      ↓
Threat Analysis
```

---

## Security Components

| Component | Purpose |
|---|---|
| Nginx Access Logs | Capture incoming traffic |
| Attack Detection Script | Detect suspicious requests |
| Security Alert Script | Generate threat alerts |
| Security Incident Logs | Store detected incidents |

---

## Security Automation Features

- suspicious request scanning
- automated threat detection
- incident logging
- security alert generation
- live traffic analysis

## Infrastructure as Code (Terraform)

### Terraform Features

- Automated EC2 provisioning
- Automated security group creation
- Reproducible infrastructure deployment
- Infrastructure lifecycle management
- Infrastructure state management

---

## Terraform Components

| File | Purpose |
|---|---|
| provider.tf | AWS provider configuration |
| variables.tf | Reusable variables |
| main.tf | Infrastructure resources |
| outputs.tf | Infrastructure outputs |
| terraform.tfvars | Variable values |

---

## Terraform Workflow

```text
Terraform Configuration
        ↓
terraform init
        ↓
terraform plan
        ↓
terraform apply
        ↓
AWS Infrastructure Created
```

---

## Infrastructure Provisioned

- EC2 Ubuntu server
- Security groups
- HTTP access
- SSH access
- outbound networking