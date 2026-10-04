def add_student(students, name):
    if not name or not name.strip():
        raise ValueError("Name must not be empty")
    students.append(name.strip())
    return students


def count_students(students):
    return len(students)


if __name__ == "__main__":
    data = []
    add_student(data, "Aidar")
    add_student(data, "Aliya")
    print("Students:", data)
    print("Total:", count_students(data))