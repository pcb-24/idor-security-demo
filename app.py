from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated Database of student records
STUDENTS = {
    "101": {"name": "Alice", "cgpa": 8.9, "private_notes": "Tuition scholarship active"},
    "102": {"name": "Bob", "cgpa": 7.1, "private_notes": "Attendance warning issued"},
    "103": {"name": "Charlie", "cgpa": 9.4, "private_notes": "Dean's list candidate"}
}

# Assume Alice is currently logged in
CURRENT_LOGGED_IN_STUDENT_ID = "101"

@app.route("/")
def home():
    return """
    <h2>IDOR Security Demonstration</h2>
    <p>Logged in as: <b>Alice (ID: 101)</b></p>
    <ul>
      <li><a href="/vulnerable/student?id=101">Vulnerable: View My Data (Alice)</a></li>
      <li><a href="/vulnerable/student?id=102">Vulnerable: View Bob's Data (IDOR Exploit)</a></li>
      <li><a href="/secure/student?id=102">Secure: Try Viewing Bob's Data (Blocked)</a></li>
    </ul>
    """

# ❌ VULNERABLE ENDPOINT: Takes 'id' from URL without verifying identity
@app.route("/vulnerable/student")
def vulnerable_student():
    student_id = request.args.get("id")
    if student_id in STUDENTS:
        return jsonify(STUDENTS[student_id])
    return jsonify({"error": "Student not found"}), 404

# ✅ SECURE ENDPOINT: Enforces Authorization before returning data
@app.route("/secure/student")
def secure_student():
    requested_id = request.args.get("id")

    # Access Control Check
    if requested_id != CURRENT_LOGGED_IN_STUDENT_ID:
        return jsonify({
            "error": "403 Forbidden",
            "message": "Access Denied: You cannot view records belonging to another student."
        }), 403

    return jsonify(STUDENTS[requested_id])

if __name__ == "__main__":
    app.run(port=5000, debug=True)
