# Deployment Steps

## Connect To EC2

```bash
ssh -i incident-response-key.pem ubuntu@PUBLIC_IP
```

---

## Activate Python Virtual Environment

```bash
source venv/bin/activate
```

---

## Run Flask Application

```bash
python app.py
```

---

## Test Application

```text
http://PUBLIC_IP:5000
```

---

# Issues Faced

## SSH Connection Timeout

### Cause
Port 22 was blocked in Security Group.

### Fix
Allowed SSH inbound rule.

---

## Flask Public Access Issue

### Cause
Flask app was listening only on localhost.

### Fix

```python
app.run(host="0.0.0.0", port=5000)
```

---

## Port 5000 Already In Use

### Cause
Flask application already running in background.

### Verification

```bash
sudo ss -tulnp | grep 5000
```

---

## Python Command Not Found

### Cause
Virtual environment was not activated.

### Fix

```bash
source venv/bin/activate
```