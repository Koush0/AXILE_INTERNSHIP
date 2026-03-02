const BACKEND_URL = "https://studentvault-backend.onrender.com";

// LOGIN
async function login() {
    const username = document.getElementById("loginUser").value;
    const password = document.getElementById("loginPass").value;

    const res = await fetch(`${BACKEND_URL}/login`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, password })
    });

    if (res.ok) {
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid credentials");
    }
}

// REGISTER
async function register() {
    const username = document.getElementById("regUser").value;
    const password = document.getElementById("regPass").value;

    const res = await fetch(`${BACKEND_URL}/register`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ username, password })
    });

    if (res.ok) {
        alert("Registration successful!");
        window.location.href = "index.html";
    } else {
        alert("User already exists");
    }
}

// LOAD STUDENTS
async function loadStudents() {
    const res = await fetch(`${BACKEND_URL}/students`);
    const data = await res.json();

    const table = document.getElementById("studentTable");
    table.innerHTML = "";

    data.forEach(student => {
        table.innerHTML += `
        <tr>
            <td>${student[1]}</td>
            <td>${student[2]}</td>
            <td>${student[3]}</td>
            <td>${student[4]}</td>
            <td>
                <button onclick="deleteStudent(${student[0]})">Delete</button>
            </td>
        </tr>
        `;
    });
}

// ADD STUDENT
async function addStudent() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const usn = document.getElementById("usn").value;
    const course = document.getElementById("course").value;

    await fetch(`${BACKEND_URL}/students`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ name, age, usn, course })
    });

    loadStudents();
}

// DELETE STUDENT
async function deleteStudent(id) {
    await fetch(`${BACKEND_URL}/students/${id}`, {
        method: "DELETE"
    });

    loadStudents();
}
