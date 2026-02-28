class Person:
    def __init__(self, name: str, age: int, person_id: str) -> None:
        self.name = name
        self.age = age
        self.person_id = person_id

    def __repr__(self) -> str:
        return f"Person(name={self.name!r}, age={self.age}, id={self.person_id!r})"

class Student(Person):
    def __init__(self, name: str, age: int, student_id: str, grade_level: str) -> None:
        super().__init__(name, age, student_id)
        self.grade_level = grade_level
        self.enrolled_courses: list[Course] = []  # type: ignore  # forward reference

    def __repr__(self) -> str:
        return (f"Student(name={self.name!r}, age={self.age}, id={self.person_id!r}, "
                f"grade_level={self.grade_level!r})")

    def enroll_in_course(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)

    def drop_course(self, course):
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)

class Course:
    def __init__(self, course_name: str, course_id: str, instructor: str) -> None:
        self.course_name = course_name
        self.course_id = course_id
        self.instructor = instructor
        self.students: list[Student] = []  # type: ignore  # forward reference

    def __repr__(self) -> str:
        return (f"Course(name={self.course_name!r}, id={self.course_id!r}, "
                f"instructor={self.instructor!r})")

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student) 

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

class StudentManagementSystem:
    def __init__(self) -> None:
        self.students: dict[str, Student] = {}
        self.courses: dict[str, Course] = {}

    def add_student(self, name, age, student_id, grade_level):
        if student_id not in self.students:
            self.students[student_id] = Student(name, age, student_id, grade_level)
            print(f"Student {name} added.")
        else:
            print("Student ID already exists.")

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print("Student removed.")
        else:
            print("Student ID not found.")

    def add_course(self, course_name, course_id, instructor):
        if course_id not in self.courses:
            self.courses[course_id] = Course(course_name, course_id, instructor)
            print(f"Course {course_name} added.")
        else:
            print("Course ID already exists.")

    def remove_course(self, course_id):
        if course_id in self.courses:
            del self.courses[course_id]
            print("Course removed.")
        else:
            print("Course ID not found.")

    def enroll_student(self, student_id, course_id):
        student = self.students.get(student_id)
        course = self.courses.get(course_id)
        if student and course:
            student.enroll_in_course(course)
            course.add_student(student)
            print(f"Student {student.name} enrolled in {course.course_name}.")
        else:
            print("Invalid student or course ID.")

    def view_student_courses(self, student_id):
        student = self.students.get(student_id)
        if student:
            print(f"{student.name}'s courses:")
            for course in student.enrolled_courses:
                print(f"- {course.course_name}")
        else:
            print("Student ID not found.")

    def view_course_students(self, course_id: str) -> None:
        course = self.courses.get(course_id)
        if course:
            print(f"Students in {course.course_name}:")
            for student in course.students:
                print(f"- {student.name}")
        else:
            print("Course ID not found.")

    def list_students(self) -> None:
        if not self.students:
            print("No students registered.")
            return
        print("Registered students:")
        for sid, student in self.students.items():
            print(f"- {student.name} (ID: {sid}, grade: {student.grade_level})")

    def list_courses(self) -> None:
        if not self.courses:
            print("No courses available.")
            return
        print("Available courses:")
        for cid, course in self.courses.items():
            print(f"- {course.course_name} (ID: {cid}, instructor: {course.instructor})")

def main():
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Add Course")
        print("4. Remove Course")
        print("5. Enroll Student in Course")
        print("6. View Student's Courses")
        print("7. View Course Roster")
        print("8. List All Students")
        print("9. List All Courses")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ").strip()
            try:
                age = int(input("Enter student age: "))
            except ValueError:
                print("Age must be a number.")
                continue
            student_id = input("Enter student ID: ").strip()
            grade_level = input("Enter grade level: ").strip()
            system.add_student(name, age, student_id, grade_level)
        elif choice == "2":
            student_id = input("Enter student ID to remove: ").strip()
            system.remove_student(student_id)
        elif choice == "3":
            course_name = input("Enter course name: ").strip()
            course_id = input("Enter course ID: ").strip()
            instructor = input("Enter instructor name: ").strip()
            system.add_course(course_name, course_id, instructor)
        elif choice == "4":
            course_id = input("Enter course ID to remove: ").strip()
            system.remove_course(course_id)
        elif choice == "5":
            student_id = input("Enter student ID: ").strip()
            course_id = input("Enter course ID: ").strip()
            system.enroll_student(student_id, course_id)
        elif choice == "6":
            student_id = input("Enter student ID: ").strip()
            system.view_student_courses(student_id)
        elif choice == "7":
            course_id = input("Enter course ID: ").strip()
            system.view_course_students(course_id)
        elif choice == "8":
            system.list_students()
        elif choice == "9":
            system.list_courses()
        elif choice == "0":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
