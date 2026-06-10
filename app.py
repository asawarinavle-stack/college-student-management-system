from flask import Flask, request

app = Flask(__name__)

students = []

@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        department = request.form['department']

        students.append({
            'name': name,
            'roll': roll,
            'department': department
        })

    student_html = ""

    for student in students:
        student_html += f"""
        <tr>
            <td>{student['name']}</td>
            <td>{student['roll']}</td>
            <td>{student['department']}</td>
        </tr>
        """

    return f"""
    <html>
    <head>
        <title>College Student Management System</title>
    </head>

    <body style="font-family: Arial; margin:40px; text-align:center;">

        <h1>🎓 College Student Management System</h1>

        <h2>CI/CD DevOps Project</h2>

        <form method="POST">

            <input type="text"
                   name="name"
                   placeholder="Enter Student Name"
                   required>

            <br><br>

            <input type="text"
                   name="roll"
                   placeholder="Enter Roll Number"
                   required>

            <br><br>

            <input type="text"
                   name="department"
                   placeholder="Enter Department"
                   required>

            <br><br>

            <button type="submit">
                Add Student
            </button>

        </form>

        <br><br>

        <h2>Student List</h2>

        <table border="1"
               align="center"
               cellpadding="10">

            <tr>
                <th>Name</th>
                <th>Roll No</th>
                <th>Department</th>
            </tr>

            {student_html}

        </table>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)