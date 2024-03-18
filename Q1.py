import psycopg


#NOTE : Make sure to run create.sql and create the table before running this file

# Global database connection
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "Rohan2002"
POSTGRES_HOST = "localhost"
POSTGRES_PORT = "5432"
conn = psycopg.connect(f"dbname=postgres user={POSTGRES_USER} host={POSTGRES_HOST} port={POSTGRES_PORT} password={POSTGRES_PASSWORD}")

# Function definitions
def getAllStudents():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM students;")
        return cur.fetchall()

def pretty_print(students):
    for student in students:
        print(student)


def addStudent(first_name, last_name, email, enrollment_date):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
            (first_name, last_name, email, enrollment_date)
        )
        conn.commit()

def updateStudentEmail(student_id, new_email):
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id)
        )
        conn.commit()

def deleteStudent(student_id):
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM students WHERE student_id = %s;",
            (student_id,)
        )
        conn.commit()


if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. View all students")
        print("2. Add a new student")
        print("3. Update a student")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        try:
            if choice == '1':
                students = getAllStudents()
                pretty_print(students)

            elif choice == '2':
                first_name = input("Enter first name: ")
                last_name = input("Enter last name: ")
                email = input("Enter email: ")
                enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
                addStudent(first_name, last_name, email, enrollment_date)
                print("Student added successfully.")

            elif choice == '3':
                student_id = int(input("Enter student ID: "))
                new_email = input("Enter new email: ")
                updateStudentEmail(student_id, new_email)
                print("Email updated successfully.")


            elif choice == '4':
                student_id = int(input("Enter student ID: "))
                deleteStudent(student_id)
                print("Student deleted successfully.")

            elif choice == '5':
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"The following error occured: {e}")
            conn.rollback() 