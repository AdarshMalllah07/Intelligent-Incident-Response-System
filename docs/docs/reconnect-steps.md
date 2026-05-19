# Reconnect Steps After Stopping EC2

## Start EC2 Instance
AWS Console → EC2 → Start Instance

Wait for:
- Running state
- 2/2 status checks passed

---

## Get Public IP

Copy new Public IPv4 address from EC2 dashboard.

---

## SSH Into Server

```bash
ssh -i incident-response-key.pem ubuntu@PUBLIC_IP
```

---

## Go To Application Directory

```bash
cd ~/app
```

---

## Activate Virtual Environment

```bash
source venv/bin/activate
```

---

## Start Flask Application

```bash
python app.py
```

---

## Test Application

```text
http://PUBLIC_IP:5000
```