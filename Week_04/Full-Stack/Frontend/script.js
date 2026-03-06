// ===============================
// CONFIG
// ===============================

const BASE_URL = "https://studentvault-backend.onrender.com";


// ===============================
// AUTH SYSTEM (CONNECTED TO BACKEND)
// ===============================

async function register() {
    const username = document.getElementById("regUser").value;
    const password = document.getElementById("regPass").value;

    if (!username || !password) {
        alert("Fill all fields");
        return;
    }

    const response = await fetch(`${BASE_URL}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok) {
        alert("Registration successful!");
        window.location.href = "index.html";
    } else {
        alert(data.error);
    }
}

async function login() {
    const username = document.getElementById("loginUser").value;
    const password = document.getElementById("loginPass").value;

    const response = await fetch(`${BASE_URL}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem("loggedIn", "true");
        window.location.href = "dashboard.html";
    } else {
        alert(data.error);
    }
}

function checkAuth() {
    if (localStorage.getItem("loggedIn") !== "true") {
        window.location.href = "index.html";
    }
}

function logout() {
    localStorage.removeItem("loggedIn");
    window.location.href = "index.html";
}


// ===============================
// STUDENT CRUD (CONNECTED TO BACKEND)
// ===============================

async function renderStudents() {
    const table = document.getElementById("studentTable");
    if (!table) return;

    const response = await fetch(`${BASE_URL}/students`);
    const students = await response.json();

    table.innerHTML = "";

    students.forEach((student) => {
        const [id, name, age, usn, course] = student;

        table.innerHTML += `
            <tr>
                <td>${name}</td>
                <td>${age}</td>
                <td>${usn}</td>
                <td>${course}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editStudent(${id}, '${name}', '${age}', '${usn}', '${course}')">Edit</button>
                    <button class="action-btn delete-btn" onclick="deleteStudent(${id})">Delete</button>
                </td>
            </tr>
        `;
    });
}

async function saveStudent() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const usn = document.getElementById("usn").value;
    const course = document.getElementById("course").value;
    const editId = document.getElementById("editIndex").value;

    if (!name || !age || !usn || !course) {
        alert("Fill all fields");
        return;
    }

    if (editId === "") {
        // ADD
        await fetch(`${BASE_URL}/students`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, age, usn, course })
        });
    } else {
        // UPDATE
        await fetch(`${BASE_URL}/students/${editId}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name, age, usn, course })
        });

        document.getElementById("editIndex").value = "";
    }

    clearForm();
    renderStudents();
}

function editStudent(id, name, age, usn, course) {
    document.getElementById("name").value = name;
    document.getElementById("age").value = age;
    document.getElementById("usn").value = usn;
    document.getElementById("course").value = course;
    document.getElementById("editIndex").value = id;
}

async function deleteStudent(id) {
    await fetch(`${BASE_URL}/students/${id}`, {
        method: "DELETE"
    });

    renderStudents();
}

function clearForm() {
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("usn").value = "";
    document.getElementById("course").value = "";
}
