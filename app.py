def get_student_data():
    name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    subjects = ["Math", "Physics", "Urdu", "English", "Computer"]
    marks = {}
    
    for subject in subjects:
        while True:
            try:
                mark = int(input(f"Enter marks for {subject}: "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break
                else:
                    print("Marks should be between 0 and 100. Try again.")
            except ValueError:
                print("Invalid input! Please enter numeric marks.")
    
    return name, roll_number, marks


def calculate_grade(percentage):
    if percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "F"
    else:
        return "Fail"


def display_report_card(name, roll_number, marks):
    total = sum(marks.values())
    total_subjects = len(marks)
    percentage = total / total_subjects
    grade = calculate_grade(percentage)
    
    report = f"\nReport Card for {name} (Roll No: {roll_number})\n"
    report += "--------------------------------\n"
    for subject, mark in marks.items():
        report += f"{subject}: {mark}\n"
    report += f"Total: {total}/{total_subjects * 100}\n"
    report += f"Percentage: {percentage:.2f}%\n"
    report += f"Grade: {grade}\n"
    
    print(report)
    return report


def save_report_to_file(students):
    with open("report_card.txt", "w") as file:
        for student in students:
            file.write(display_report_card(*student) + "\n")
    print("\nAll report cards saved to 'report_card.txt'\n")


def main():
    students = []
    while True:
        name, roll_number, marks = get_student_data()
        students.append((name, roll_number, marks))
        print(f"Record of {name} inserted successfully!\n")
        if input("Add another student? (Y/N): ").strip().upper() != 'Y':
            break
    
    print("\nGenerating Report Cards...")
    for student in students:
        display_report_card(*student)
    
    save_report_to_file(students)


if __name__ == "__main__":
    main()
