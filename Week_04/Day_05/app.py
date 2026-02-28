from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Insert default user (only if table empty)
    cursor.execute("SELECT * FROM Users")
    if not cursor.fetchall():
        cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)",
                       ("koush_wastaken", "1234"))

    conn.commit()
    conn.close()

init_db()

# Login Page
@app.route("/")
def login_page():
    return render_template("login.html")

# Handle Login
@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE username=? AND password=?",
                   (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        return redirect("/dashboard")
    else:
        return "Invalid Username or Password <br><br><a href='/'>Try Again</a>"

# Dashboard Page
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
