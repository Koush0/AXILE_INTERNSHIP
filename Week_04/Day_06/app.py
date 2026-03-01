from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Add Record Page
@app.route("/")
def add_page():
    return render_template("add.html")

# Insert Record
@app.route("/add", methods=["POST"])
def add():
    name = request.form["name"]
    age = request.form["age"]
    course = request.form["course"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Students (name, age, course) VALUES (?, ?, ?)",
                   (name, age, course))

    conn.commit()
    conn.close()

    return redirect("/view")

# View Records
@app.route("/view")
def view():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Students")
    data = cursor.fetchall()

    conn.close()

    return render_template("view.html", records=data)


@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect("/view")

# Edit Page
@app.route("/edit/<int:id>")
def edit(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Students WHERE id=?", (id,))
    record = cursor.fetchone()

    conn.close()

    return render_template("edit.html", record=record)

# Update Record
@app.route("/update/<int:id>", methods=["POST"])
def update(id):
    name = request.form["name"]
    age = request.form["age"]
    course = request.form["course"]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE Students SET name=?, age=?, course=? WHERE id=?",
                   (name, age, course, id))

    conn.commit()
    conn.close()

    return redirect("/view")

if __name__ == "__main__":
    app.run(debug=True)
