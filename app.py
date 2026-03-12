from flask import Flask, jsonify, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Sample data
students = [
    {"id": 1, "name": "Cristian", "grade": 85, "section": "Firebase"},
    {"id": 2, "name": "Chalzy", "grade": 90, "section": "Firebase"}
]

# Home route
@app.route('/')
def home():
    return redirect(url_for('list_students'))

# View students
@app.route('/students')
def list_students():
    html = """
    <h2>Student List</h2>

    <a href="/add_student_form">Add Student</a>
    <br><br>

    <ul>
    {% for s in students %}
        <li>
        {{s["id"]}} - {{s["name"]}} (Grade: {{s["grade"]}}, Section: {{s["section"]}})
        <a href="/edit_student/{{s['id']}}">Edit</a>
        </li>
    {% endfor %}
    </ul>
    """
    return render_template_string(html, students=students)

# Add student form
@app.route('/add_student_form')
def add_student_form():
    html = """
    <h2>Add Student</h2>

    <form action="/add_student" method="POST">
        Name:<br>
        <input type="text" name="name"><br><br>

        Grade:<br>
        <input type="number" name="grade"><br><br>

        Section:<br>
        <input type="text" name="section"><br><br>

        <button type="submit">Add</button>
    </form>

    <br>
    <a href="/students">Back</a>
    """
    return render_template_string(html)

# Add student
@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form.get("name")
    grade = request.form.get("grade")
    section = request.form.get("section")

    new_id = len(students) + 1

    new_student = {
        "id": new_id,
        "name": name,
        "grade": int(grade),
        "section": section
    }

    students.append(new_student)

    return redirect(url_for('list_students'))

# Edit student
@app.route('/edit_student/<int:id>', methods=['GET', 'POST'])
def edit_student(id):

    student = next((s for s in students if s["id"] == id), None)

    if student is None:
        return "Student not found"

    if request.method == "POST":
        student["name"] = request.form["name"]
        student["grade"] = int(request.form["grade"])
        student["section"] = request.form["section"]

        return redirect(url_for('list_students'))

    html = """
    <h2>Edit Student</h2>

    <form method="POST">
        Name:<br>
        <input type="text" name="name" value="{{student['name']}}"><br><br>

        Grade:<br>
        <input type="number" name="grade" value="{{student['grade']}}"><br><br>

        Section:<br>
        <input type="text" name="section" value="{{student['section']}}"><br><br>

        <button type="submit">Update</button>
    </form>

    <br>
    <a href="/students">Back</a>
    """

    return render_template_string(html, student=student)


if __name__ == "__main__":
    app.run(debug=True)
