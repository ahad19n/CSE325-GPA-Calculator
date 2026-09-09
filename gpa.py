import json
import os

DATA_FILE = "courses.json"
VALID_CREDIT_HOURS = {"0", "1", "2", "3", "4"}
VALID_GPA = {"0", "1", "1.33", "1.66", "2", "2.33", "2.66", "3", "3.33", "3.66", "4"}


def prompt_choice(prompt, valid_values):
    while True:
        value = input(prompt).strip()
        if value in valid_values:
            return value
        print(f"Invalid input. Valid options: {', '.join(sorted(valid_values))}")


def load_courses():
    if not os.path.exists(DATA_FILE):
        print(f"No saved data found ({DATA_FILE} does not exist).")
        return {}
    with open(DATA_FILE) as f:
        return json.load(f)


def save_courses(courses):
    with open(DATA_FILE, "w") as f:
        json.dump(courses, f, indent=2)
    print(f"Saved {len(courses)} course(s) to {DATA_FILE}.")


def add_course(courses):
    name = input("Enter course name: ").strip()
    while not name:
        name = input("Course name cannot be empty. Enter course name: ").strip()

    if name in courses:
        confirm = input(f'"{name}" already exists. Overwrite? (y/n): ').strip().lower()
        if confirm != "y":
            print("Skipped.")
            return

    credit_hours = prompt_choice(
        "Enter credit hours (0, 1, 2, 3, 4): ", VALID_CREDIT_HOURS
    )
    gpa = prompt_choice(
        "Enter GPA received (0, 1, 1.33, 1.66, 2, 2.33, 2.66, 3, 3.33, 3.66, 4): ",
        VALID_GPA,
    )

    courses[name] = {"credit_hours": int(credit_hours), "gpa": float(gpa)}
    print(f'Added "{name}".')


def calculate_gpa(courses):
    if not courses:
        print("No courses entered yet.")
        return

    total_points = sum(c["credit_hours"] * c["gpa"] for c in courses.values())
    total_hours = sum(c["credit_hours"] for c in courses.values())

    if total_hours == 0:
        print("Total credit hours are 0, cannot calculate GPA.")
        return

    print(f"GPA: {total_points / total_hours:.2f}")


def list_courses(courses):
    if not courses:
        print("No courses entered yet.")
        return
    for name, c in courses.items():
        print(f"  {name}: {c['credit_hours']} credit hours, {c['gpa']} GPA")


def print_menu():
    print()
    print("Commands:")
    print("  add     - enter a new course")
    print("  list    - show entered courses")
    print("  calc    - calculate GPA")
    print("  save    - save courses to file")
    print("  load    - load courses from file (replaces current list)")
    print("  exit    - quit")
    print()


def main():
    courses = {}
    print("=== GPA Calculator ===")

    if os.path.exists(DATA_FILE):
        choice = input(f"Found saved data in {DATA_FILE}. Load it? (y/n): ").strip().lower()
        if choice == "y":
            courses = load_courses()

    print_menu()
    while True:
        cmd = input("> ").strip().lower()
        if cmd == "add":
            add_course(courses)
        elif cmd == "list":
            list_courses(courses)
        elif cmd == "calc":
            calculate_gpa(courses)
        elif cmd == "save":
            save_courses(courses)
        elif cmd == "load":
            courses = load_courses()
        elif cmd == "exit":
            break
        else:
            print("Unknown command.")
            print_menu()


if __name__ == "__main__":
    main()
