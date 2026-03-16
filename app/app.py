from flask import Flask, render_template, request
import mysql.connector
import os

app = Flask(__name__)

db = mysql.connector.connect(
    host=os.environ.get("DB_HOST"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME")
)

cursor = db.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
 id INT AUTO_INCREMENT PRIMARY KEY,
 task VARCHAR(255)
)
""")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        task = request.form["task"]
        cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
        db.commit()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    return render_template("index.html", tasks=tasks)

app.run(host="0.0.0.0", port=5000)
