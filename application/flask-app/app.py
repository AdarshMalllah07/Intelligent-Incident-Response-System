from database import get_db_connection
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Intelligent Incident Response System Running"

@app.route("/health")
@app.route("/incidents")
def incidents():

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            incident_type,
            severity,
            status,
            description,
            created_at
        FROM incidents
        ORDER BY created_at DESC
    """)

    incidents = cursor.fetchall()

    incident_list = []

    for incident in incidents:
        incident_list.append({
            "id": incident[0],
            "incident_type": incident[1],
            "severity": incident[2],
            "status": incident[3],
            "description": incident[4],
            "created_at": str(incident[5])
        })

    cursor.close()
    connection.close()

    return {
        "incidents": incident_list
    }
def health():
    return {
        "status": "healthy"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)