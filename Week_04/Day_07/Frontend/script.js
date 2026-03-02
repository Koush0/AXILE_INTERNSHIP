// ===============================
// AUTH SYSTEM
// ===============================

function register() {
    const user = document.getElementById("regUser").value;
    const pass = document.getElementById("regPass").value;

    if (!user || !pass) {
        alert("Fill all fields");
        return;
    }

    localStorage.setItem("user", user);
    localStorage.setItem("pass", pass);

    alert("Registration successful!");
    window.location.href = "index.html";
}

function login() {
    const user = document.getElementById("loginUser").value;
    const pass = document.getElementById("loginPass").value;

    const savedUser = localStorage.getItem("user");
    const savedPass = localStorage.getItem("pass");

    if (user === savedUser && pass === savedPass) {
        localStorage.setItem("loggedIn", "true");
        window.location.href = "dashboard.html";
    } else {
        alert("Invalid credentials");
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
// STUDENT CRUD SYSTEM
// ===============================

// Always get fresh students from localStorage
function getStudents() {
    return JSON.parse(localStorage.getItem("students")) || [];
}

// Render student table
function renderStudents() {
    const table = document.getElementById("studentTable");
    if (!table) return;

    const students = getStudents();
    table.innerHTML = "";

    students.forEach((student, index) => {
        table.innerHTML += `
            <tr>
                <td>${student.name}</td>
                <td>${student.age}</td>
                <td>${student.usn}</td>
                <td>${student.course}</td>
                <td>
                    <button class="action-btn edit-btn" onclick="editStudent(${index})">Edit</button>
                    <button class="action-btn delete-btn" onclick="deleteStudent(${index})">Delete</button>
                </td>
            </tr>
        `;
    });
}

// Save or Update student
function saveStudent() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const usn = document.getElementById("usn").value;
    const course = document.getElementById("course").value;
    const editIndex = document.getElementById("editIndex").value;

    if (!name || !age || !usn || !course) {
        alert("Fill all fields");
        return;
    }

    let students = getStudents();
    const studentData = { name, age, usn, course };

    if (editIndex === "") {
        students.push(studentData);
    } else {
        students[editIndex] = studentData;
        document.getElementById("editIndex").value = "";
    }

    localStorage.setItem("students", JSON.stringify(students));
    clearForm();
    renderStudents();
}

// Edit student
function editStudent(index) {
    const students = getStudents();
    const student = students[index];

    document.getElementById("name").value = student.name;
    document.getElementById("age").value = student.age;
    document.getElementById("usn").value = student.usn;
    document.getElementById("course").value = student.course;
    document.getElementById("editIndex").value = index;
}

// Delete student
function deleteStudent(index) {
    let students = getStudents();
    students.splice(index, 1);
    localStorage.setItem("students", JSON.stringify(students));
    renderStudents();
}

// Clear form
function clearForm() {
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("usn").value = "";
    document.getElementById("course").value = "";
}
