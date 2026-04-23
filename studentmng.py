class Student:

    all_students = []

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def show(self):
        print(f"\nName: {self.name} | Roll: {self.roll} | Marks: {self.marks}")

    @classmethod
    def find_student_by_roll(cls, roll):
        for student in cls.all_students:
            if student.roll == roll:  
                return student
        return None

    @classmethod
    def add(cls):
        name = input("Name: ").strip()
        roll = input("Roll: ").strip()

        if not name or not roll:
            raise ValueError("Name/Roll cannot be empty")

        if cls.find_student_by_roll(roll):
            raise ValueError("Roll already exists")

        try:
            marks = int(input("Marks: "))
        except ValueError:
            raise ValueError("Marks must be a number")

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be 0-100")

        cls.all_students.append(cls(name, roll, marks))
        print("Student added!")

    @classmethod
    def update_marks(cls):
        roll = input("Enter roll: ").strip()
        student = cls.find_student_by_roll(roll)

        if not student:
            raise ValueError("Student not found")

        try:
            marks = int(input("New marks: "))
        except ValueError:
            raise ValueError("Marks must be a number")

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be 0-100")

        student.marks = marks
        print("Marks updated!")

    @classmethod
    def show_all(cls):
        if not cls.all_students:
            print("No students found")
        else:
            for s in cls.all_students:
                s.show()

    @classmethod
    def sort_by_name(cls):  
        cls.all_students.sort(key=lambda x: x.name.lower())
        print("Sorted by name")
        cls.show_all()

    @classmethod
    def sort_by_marks(cls): 
        cls.all_students.sort(key=lambda x: x.marks, reverse=True)
        print("Sorted by marks")
        cls.show_all()

    @classmethod
    def report(cls):
        if not cls.all_students:
            print("No data available") 
            return

        marks = [s.marks for s in cls.all_students]
        avg = sum(marks) / len(marks)

        topper = max(cls.all_students, key=lambda s: s.marks)
        lowest = min(cls.all_students, key=lambda s: s.marks)

        print("\n--- REPORT ---")
        print(f"Total: {len(cls.all_students)} | Avg: {avg:.2f}")
        print(f"Topper: {topper.name} ({topper.marks})")
        print(f"Lowest: {lowest.name} ({lowest.marks})")


#  Login
def login():
    user = input("Username: ").strip()
    pwd = input("Password: ").strip()

    if user.lower() != "Suneel".lower() or pwd != "suneel@9399":
        raise ValueError("Invalid login")


def menu():
    try:
        login()
        print("Login successful!")

        while True:
            print("\n1.Add 2.Update 3.Show 4.SortName 5.SortMarks 6.Report 7.Exit")
            choice = input("Choice: ").strip()

            if choice == '1':
                Student.add()
            elif choice == '2':
                Student.update_marks()
            elif choice == '3':
                Student.show_all()
            elif choice == '4':
                Student.sort_by_name()
            elif choice == '5':
                Student.sort_by_marks()
            elif choice == '6':
                Student.report()
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice")

    except ValueError as e:
        print("Error:", e)
    except KeyboardInterrupt:
        print("\nExited safely")


if __name__ == "__main__":
    menu()