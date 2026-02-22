<!DOCTYPE html>
<html>
<head>
    <title>JavaScript Interactive Page</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background: #0f0f0f;
            font-family: Arial, sans-serif;
            text-align: center;
            padding: 40px;
        }

        .main-title {
            color: #00ffcc;
            font-size: 40px;
            margin-bottom: 40px;
            text-shadow: 0 0 15px #00ffcc;
        }

        .card {
            background: #1c1c1c;
            padding: 40px;
            margin: 30px auto;
            width: 80%;
            max-width: 600px;
            border-radius: 20px;
            box-shadow: 0 0 25px rgba(0, 255, 204, 0.4);
            transition: 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
        }

        button {
            background: #00ffcc;
            border: none;
            padding: 12px 25px;
            border-radius: 30px;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s ease;
            margin-top: 15px;
        }

        button:hover {
            background: #00ccaa;
        }

        input {
            padding: 10px;
            width: 70%;
            margin: 10px 0;
            border-radius: 10px;
            border: none;
            text-align: center;
        }

        p {
            color: white;
            font-size: 18px;
        }

        h2 {
            color: white;
            margin-bottom: 15px;
        }
    </style>

</head>

<body>

    <h1 class="main-title">JavaScript Interactive Page</h1>

    <!-- 1. Alert Section -->
    <div class="card">
        <h2>Alert Example</h2>
        <button onclick="showAlert()">Click for Alert</button>
    </div>

    <!-- 2. Change Text -->
    <div class="card">
        <h2>Change Text</h2>
        <p id="changeText">Click the button to change this text.</p>
        <button onclick="changeText()">Change Text</button>
    </div>

    <!-- 3. Date & Time -->
    <div class="card">
        <h2>Date & Time</h2>
        <p id="dateTime">Click to display current date & time</p>
        <button onclick="showDateTime()">Show Date & Time</button>
    </div>

    <!-- 4. Calculator -->
    <div class="card">
        <h2>Add Two Numbers</h2>
        <input type="number" id="num1" placeholder="Enter first number">
        <input type="number" id="num2" placeholder="Enter second number">
        <br>
        <button onclick="addNumbers()">Add</button>
        <p id="result"></p>
    </div>

    <!-- 5. Form Validation -->
    <div class="card">
        <h2>Form Validation</h2>
        <form onsubmit="return validateForm()">
            <input type="text" id="username" placeholder="Enter your name">
            <br>
            <button type="submit">Submit</button>
        </form>
    </div>

    <script>
        // 1. Alert
        function showAlert() {
            alert("Button clicked successfully!");
        }

        // 2. Change Text
        function changeText() {
            document.getElementById("changeText").innerHTML =
                "Text changed successfully using JavaScript!";
        }

        // 3. Show Date & Time
        function showDateTime() {
            let now = new Date();
            document.getElementById("dateTime").innerHTML = now;
        }

        // 4. Calculator
        function addNumbers() {
            let n1 = Number(document.getElementById("num1").value);
            let n2 = Number(document.getElementById("num2").value);

            let sum = n1 + n2;

            document.getElementById("result").innerHTML = "Result: " + sum;
        }

        // 5. Form Validation
        function validateForm() {
            let name = document.getElementById("username").value;

            if (name === "") {
                alert("Name cannot be empty!");
                return false;
            } else {
                alert("Form submitted successfully!");
                return true;
            }
        }
    </script>

</body>
</html>
