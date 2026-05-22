# Security Monitoring & Intrusion Detection

## Objective

Implement basic intrusion detection and security monitoring for the Intelligent Incident Response System.

---

# Why Security Monitoring Matters

Public servers continuously receive:
- vulnerability scans
- exploit attempts
- automated probes
- malicious traffic

Security monitoring helps identify suspicious behavior before incidents escalate.

---

# Security Monitoring Architecture

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

# Attack Detection Script

## Script Location

```text
/home/ubuntu/security-monitoring/detect-attacks.sh
```

---

# Detection Script

```bash
#!/bin/bash

ACCESS_LOG="/var/log/nginx/access.log"
SECURITY_LOG="/home/ubuntu/security-monitoring/security-incidents.log"

echo "===== Security Scan Started: $(date) =====" >> $SECURITY_LOG

grep -Ei "phpunit|wp-admin|xmlrpc|eval|vendor|cgi-bin" $ACCESS_LOG >> $SECURITY_LOG

echo "" >> $SECURITY_LOG
```

---

# Threat Patterns Monitored

| Pattern | Description |
|---|---|
| phpunit | PHP vulnerability scanning |
| wp-admin | WordPress admin probing |
| xmlrpc | WordPress brute-force attempts |
| vendor | Laravel/PHP exploit attempts |
| cgi-bin | CGI exploit scanning |

---

# Run Security Detection

```bash
./detect-attacks.sh
```

---

# View Security Incidents

```bash
cat security-incidents.log
```

---

# Security Alert Script

## Script Location

```text
/home/ubuntu/security-monitoring/security-alert.sh
```

---

# Alert Script

```bash
#!/bin/bash

INCIDENT_COUNT=$(grep -Ei "phpunit|wp-admin|xmlrpc|vendor" /var/log/nginx/access.log | wc -l)

if [ "$INCIDENT_COUNT" -gt 5 ]; then
    echo "$(date) - WARNING: High suspicious traffic detected. Count: $INCIDENT_COUNT" >> /home/ubuntu/security-monitoring/security-alerts.log
fi
```

---

# Live Traffic Monitoring

```bash
sudo tail -f /var/log/nginx/access.log
```

---

# Security Concepts Learned

- security observability
- intrusion detection
- log analysis
- signature-based detection
- threat telemetry
- attack pattern monitoring
- operational security