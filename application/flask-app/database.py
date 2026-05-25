import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "incident_response",
    "user": "incident_admin",
    "password": "StrongPassword123"
}

def get_db_connection():
    connection = psycopg2.connect(
        host=DB_CONFIG["host"],
        database=DB_CONFIG["database"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
    )

    return connection