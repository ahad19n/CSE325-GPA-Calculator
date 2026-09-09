import json
import os

VALID_CREDIT_HOURS = {0, 1, 2, 3, 4}
VALID_GPA_VALUES = {0, 1, 1.33, 1.66, 2, 2.33, 2.66, 3, 3.33, 3.66, 4}
DEFAULT_SAVE_FILE = "courses.json"


def prompt_credit_hours():
    while True:
        raw = input(f"Enter credit hours {sorted(VALID_CREDIT_HOURS)}: ").strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a whole number.")
            continue
        if value not in VALID_CREDIT_HOURS:
            print(f"Credit hours must be one of {sorted(VALID_CREDIT_HOURS)}.")
            continue
        return value


def prompt_gpa():
    while True:
        raw = input(f"Enter GPA received {sorted(VALID_GPA_VALUES)}: ").strip()
        try:
            value = round(float(raw), 2)
        except ValueError:
            print("Please enter a number.")
            continue
        if value not in VALID_GPA_VALUES:
            print(f"GPA must be one of {sorted(VALID_GPA_VALUES)}.")
            continue
        return value


def add_course(courses):
    name = input("Enter course name: ").strip()
    credit_hours = prompt_credit_hours()
    gpa = prompt_gpa()
    courses.append({"name": name, "credit_hours": credit_hours, "gpa": gpa})
    print(f"Added {name}.\n")


def list_courses(courses):
    if not courses:
        print("No courses added yet.\n")
        return
    print("\nCourses:")
    for i, course in enumerate(courses, start=1):
        print(f"  {i}. {course['name']} - {course['credit_hours']} credit hours - {course['gpa']} GPA")
    print()


def calculate_gpa(courses):
    total_credit_hours = sum(c["credit_hours"] for c in courses)
    if total_credit_hours == 0:
        print("Cannot calculate GPA: total credit hours is 0.\n")
        return
    total_points = sum(c["credit_hours"] * c["gpa"] for c in courses)
    gpa = total_points / total_credit_hours
    print(f"Your GPA is: {gpa:.2f}\n")


def save_courses(courses):
    filename = input(f"Enter filename to save to [{DEFAULT_SAVE_FILE}]: ").strip() or DEFAULT_SAVE_FILE
    with open(filename, "w") as f:
        json.dump(courses, f, indent=2)
    print(f"Saved {len(courses)} course(s) to {filename}.\n")


def load_courses():
    filename = input(f"Enter filename to load from [{DEFAULT_SAVE_FILE}]: ").strip() or DEFAULT_SAVE_FILE
    if not os.path.exists(filename):
        print(f"No such file: {filename}\n")
        return []
    with open(filename, "r") as f:
        courses = json.load(f)
    print(f"Loaded {len(courses)} course(s) from {filename}.\n")
    return courses


def print_menu():
    print("1. Add course")
    print("2. View courses")
    print("3. Calculate GPA")
    print("4. Save courses")
    print("5. Load courses")
    print("6. Exit")


def main():
    courses = []
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        print()
        if choice == "1":
            add_course(courses)
        elif choice == "2":
            list_courses(courses)
        elif choice == "3":
            calculate_gpa(courses)
        elif choice == "4":
            save_courses(courses)
        elif choice == "5":
            courses = load_courses()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.\n")


if __name__ == "__main__":
    main()
