# EC2 Setup Documentation

## AWS Region
ap-south-1 (Mumbai)

## Instance Type
t2.micro

## OS
Ubuntu 24.04 LTS

# Issues Faced

## SSH Timeout Issue
### Cause
Security group missing SSH rule.

### Fix
Allowed port 22 in inbound rules.

---

## Flask Public Access Issue
### Cause
Flask bound to localhost only.

### Fix
Used:
```python
app.run(host="0.0.0.0", port=5000)
```

---

## Port Conflict Issue
### Cause
Flask already running on port 5000.

### Fix
Verified running process using:
```bash
sudo ss -tulnp | grep 5000
```