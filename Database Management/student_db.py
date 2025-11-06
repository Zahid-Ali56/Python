import pickle
import os

# ----------------------------
# Student Class
# ----------------------------
class Student:
    def __init__(self, name, department, year, roll_number):
        self.name = name
        self.department = department
        self.year = year
        self.roll_number = roll_number

    def __str__(self):
        return f"{self.roll_number} - {self.name} ({self.department}, Year {self.year})"


# ----------------------------
# Student Database Manager
# ----------------------------
class StudentDB:
    def __init__(self, filename="students.pkl"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        """Load student data from pickle file"""
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as f:
                return pickle.load(f)
        return []

    def save_data(self):
        """Save student data to pickle file"""
        with open(self.filename, "wb") as f:
            pickle.dump(self.students, f)

    def add_student(self, name, department, year, roll_number):
        """Add a new student"""
        student = Student(name, department, year, roll_number)
        self.students.append(student)
        self.save_data()
        print(f"\n✅ Student '{name}' added successfully!")

    def delete_student(self, roll_number):
        """Delete a student by roll number"""
        for s in self.students:
            if s.roll_number == roll_number:
                self.students.remove(s)
                self.save_data()
                print(f"\n❌ Student '{s.name}' deleted successfully!")
                return
        print("\n⚠️ No student found with that roll number.")

    def view_students(self):
        """Display all students"""
        if not self.students:
            print("\n📭 No students found.")
            return
        print("\n🎓 Mehran University Student Records:")
        print("-" * 60)
        for s in self.students:
            print(s)
        print("-" * 60)


# ----------------------------
# Main Menu
# ----------------------------
def main():
    db = StudentDB()

    while True:
        print("\n====== Mehran University Student Management ======")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View All Students")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            name = input("Enter Student Name: ")
            department = input("Enter Department: ")
            year = input("Enter Year: ")
            roll_number = input("Enter Roll Number: ")
            db.add_student(name, department, year, roll_number)

        elif choice == "2":
            roll_number = input("Enter Roll Number to Delete: ")
            db.delete_student(roll_number)

        elif choice == "3":
            db.view_students()

        elif choice == "4":
            print("\n👋 Exiting... Data saved successfully.")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
