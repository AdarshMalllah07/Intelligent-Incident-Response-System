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