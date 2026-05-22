# Architecture

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
AWS CloudWatch Monitoring
```

---

# Components

## EC2
Cloud-hosted Linux server.

## Flask
Backend application service.

## systemd
Linux service manager controlling Flask lifecycle.

## Nginx
Reverse proxy handling public traffic.

## CloudWatch Agent
Collects server metrics and telemetry.

## CloudWatch
AWS monitoring and observability platform.
```

# Extended Incident Response Architecture

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
Auto Remediation Script

# Logging & Observability Architecture

```text
Internet
   ↓
Nginx Reverse Proxy
   ↓
Flask Application Service
   ↓
Flask Logs + Nginx Logs
   ↓
CloudWatch Agent
   ↓
CloudWatch Logs
```
```
# Security Monitoring Architecture

```text
Internet
   ↓
Nginx Reverse Proxy
   ↓
Nginx Access Logs
   ↓
Security Detection Scripts
   ↓
Security Incident Logs
   ↓
Threat Analysis
```