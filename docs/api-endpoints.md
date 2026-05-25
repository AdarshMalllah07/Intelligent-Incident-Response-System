# API Endpoints

## Health Endpoint

```http
GET /health
```

Returns application health status.

---

## Incident Endpoint

```http
GET /incidents
```

Returns stored incident records from PostgreSQL database.

---

# Response Format

```json
{
  "incidents": []
}
```