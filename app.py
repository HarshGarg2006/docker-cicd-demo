from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "mydatabase"),
        user=os.getenv("DB_USER", "admin"),
        password=os.getenv("DB_PASSWORD", "admin123")
    )

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY
        )
    """)

    cur.execute("INSERT INTO visits DEFAULT VALUES")
    cur.execute("SELECT COUNT(*) FROM visits")

    count = cur.fetchone()[0]

    conn.commit()
    cur.close()
    conn.close()

    return f"""
    <h1>Hello from Docker Compose!</h1>
    <h2>Web + Database Application</h2>
    <p>Database connected successfully!</p>
    <h3>Total Visits: {count}</h3>
    <hr>
    <h3>Created & Developed by: Harsh Garg</h3>
    <p>Technology: Docker, Flask, PostgreSQL</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)