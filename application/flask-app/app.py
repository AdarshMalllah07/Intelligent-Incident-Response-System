from flask import Flask
from flask import render_template

from database import get_db_connection

app = Flask(__name__)


@app.route("/")
def home():

    return "Intelligent Incident Response System Running"


@app.route("/health")
def health():

    return {
        "status": "healthy"
    }


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

    incident_records = cursor.fetchall()

    incident_list = []

    for incident in incident_records:

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


@app.route("/dashboard")
def dashboard():

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

    incident_records = cursor.fetchall()

    incident_list = []

    for incident in incident_records:

        incident_list.append({
            "id": incident[0],
            "incident_type": incident[1],
            "severity": incident[2],
            "status": incident[3],
            "description": incident[4],
            "created_at": incident[5]
        })

    cursor.close()
    connection.close()

    return render_template(
        "dashboard.html",
        incidents=incident_list
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000
    )