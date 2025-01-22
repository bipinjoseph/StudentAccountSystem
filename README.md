# Student Management System

## Overview
This Python program provides a comprehensive **Student Management System** that allows users to:
- Add new student profiles.
- Log in to a student's account to perform actions like:
  - View student details.
  - Add and update marks.
  - Generate results with grades and CGPA.
  - Send results via email and SMS.
  - Delete a student account.
- View a list of all students.

The system is designed with an interactive menu-based interface for ease of use.

---

## Features

### 1. Add New Student
- Create a new student profile with details like:
  - Name
  - Admission number
  - Class
  - Address
  - Date of Birth
  - Email (Student and Parent)
  - Phone number

### 2. Student Account Login
- Log in using the **admission number** and **date of birth**.
- Post-login actions include:

#### a. View Student Details
- View a detailed profile, including:
  - Name
  - Class
  - Marks for individual subjects
  - Total marks

#### b. Add Marks
- Add marks for:
  - Physics
  - Chemistry
  - English
  - Maths
  - Biology

#### c. Generate Result
- Calculate grades for individual subjects and overall performance based on:
  - Marks obtained
  - Grade ranges
  - CGPA
- Display a formatted result sheet.

#### d. Update Marks
- Modify previously entered marks for any subject.

#### e. Send Result
- Send the result to the student's and parent's email addresses using **SMTP**.
- Deliver the result as an SMS to the student's phone number using **Twilio**.

#### f. Delete Student
- Remove the student's profile from the system.

#### g. Logout
- Exit the student account and return to the main menu.

### 3. List All Students
- Display a summary of all students currently in the system.

### 4. Exit
- Safely terminate the program.

---

## Code Structure

### Class: `Studentaccount`
This class represents the blueprint for student profiles and includes methods to:
- Add and update marks.
- Calculate grades, CGPA, and generate result sheets.
- Display student details.

### Functions
#### `select()`
- Main control flow for navigating through the program’s features.
- Implements the menu-based interface.

#### Nested Methods
- `calculate()` within `Studentaccount` handles grade calculation and result generation.
- Email and SMS functionality integrated using **SMTP** and **Twilio** APIs.

---

## Setup Instructions

### Prerequisites
- Python 3.x
- Installed libraries:
  - `smtplib`
  - `email`
  - `twilio`

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/student-management-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd student-management-system
   ```
3. Install required dependencies:
   ```bash
   pip install twilio
   ```

### Configuration
1. Update the **email sender credentials** in the `send_email` function:
   ```python
   sender = "your-email@gmail.com"
   password = "your-app-password"
   ```
2. Configure **Twilio credentials**:
   ```python
   account_sid = 'your-account-sid'
   auth_token = 'your-auth-token'
   ```

### Running the Program
Execute the script:
```bash
python student_management.py
```

---

## Usage
- Follow the interactive prompts to add students, log in, manage marks, and generate results.
- Ensure the email and phone credentials are valid to send notifications successfully.

---

## Grading System

### Individual Subject Grades
| Marks Range | Grade |
|-------------|-------|
| 90 - 100    | A     |
| 80 - 89     | B     |
| 70 - 79     | C     |
| 60 - 69     | D     |
| 50 - 59     | E     |
| Below 50    | F     |

### Overall Grades
| Total Marks Range | Grade | Status  |
|-------------------|-------|---------|
| 450 - 500         | A     | Passed  |
| 400 - 449         | B     | Passed  |
| 350 - 399         | C     | Passed  |
| 200 - 349         | D     | Passed  |
| 151 - 199         | E     | Passed  |
| Below 150         | F     | Failed  |

---

## Future Enhancements
- Add a database for persistent data storage.
- Improve user authentication with passwords.
- Integrate a web or GUI-based front-end interface.
- Add more comprehensive error handling.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgments
- [Twilio](https://www.twilio.com/) for SMS services.
- Python's built-in **SMTP** library for email functionality.

