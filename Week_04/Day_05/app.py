from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Create table
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

# Home Page
@app.route("/")
def home():
    return render_template("form.html")

# Insert Data
@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Contacts (name, email) VALUES (?, ?)", (name, email))

    conn.commit()
    conn.close()

    return '''
Data Stored Successfully! <br><br>
<a href="/">Go Back</a> <br>
<a href="/view">View Data</a>
'''

# View Data
@app.route("/view")
def view():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Contacts")
    data = cursor.fetchall()

    conn.close()

    return render_template("display.html", records=data)

# Delete Data
@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Contacts WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return '''
Record Deleted Successfully! <br><br>
<a href="/view">Go Back</a>
'''

# Edit Page
@app.route("/edit/<int:id>")
def edit(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Contacts WHERE id = ?", (id,))
    record = cursor.fetchone()

    conn.close()

    return render_template("edit.html", record=record)

# Update Data
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    email = request.form["email"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Contacts SET name = ?, email = ? WHERE id = ?", (name, email, id))

    conn.commit()
    conn.close()

    return '''
Record Updated Successfully! <br><br>
<a href="/view">View Data</a>
'''

if __name__ == "__main__":
    app.run(debug=True)
