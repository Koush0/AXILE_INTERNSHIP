from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create table if not exists
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Contacts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home page (form)
@app.route("/")
def home():
    return render_template("form.html")


# Handle form submission
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Contacts (name, email) VALUES (?, ?)",
                   (name, email))

    conn.commit()
    conn.close()

    return '''
Data stored successfully! <br><br>
<a href="/">Go Back</a> <br>
<a href="/view">View Stored Data</a>
'''


# View stored data
@app.route("/view")
def view():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Contacts")
    data = cursor.fetchall()

    conn.close()

    return str(data)


if __name__ == "__main__":
    app.run(debug=True)
