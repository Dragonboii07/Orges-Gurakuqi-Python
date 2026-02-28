<<<<<<< HEAD
# Orges-Gurakuqi-Python
=======
# Student Management System

This is a simple command-line student management system written in Python.  It allows you to
add/remove students and courses, enroll students in courses, and view rosters.

## Features

- `Person`, `Student`, and `Course` classes with helpful `__repr__` methods.
- `StudentManagementSystem` class that tracks students and courses in dictionaries.
- Menu-based CLI with input validation.
- Commands to list all students or courses for quick inspection.

## Requirements

- Python 3.11+ (3.14 used during development).

## Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/Dragonboii07/Orges-Gurakuqi-Python.git
   cd "Orges-Gurakuqi-Python"
   ```

2. **Select a Python interpreter**
   In VS Code, open the command palette (`Ctrl+Shift+P`) and choose "Python: Select Interpreter".
   Pick a valid Python installation or create/activate a virtual environment.

3. **Run the script**
   ```bash
   python "orges_project (1).py"
   ```

   A numbered menu will appear; enter a number to perform an action.  Example:
   - `1` to add a student
   - `5` to enroll a student in a course
   - `8` to list all students, etc.

4. **Commit your changes**
   ```bash
   git add README.md "orges_project (1).py"
   git commit -m "Add README and improve code"
   git push origin main
   ```

## Improvements Included

- Added type hints for clarity and better tooling support.
- Implemented `__repr__` on model classes for easier debugging.
- Added menu options to list all students/courses.
- Input validation for age and stripped whitespace.

## License

This project is released under the [MIT License](LICENSE) (add one if desired).

---

Feel free to extend the system with file persistence, a GUI, or web interface!
>>>>>>> c688c0a (Add README and polish system)
