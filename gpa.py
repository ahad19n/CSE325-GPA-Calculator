import json

def welcome_message():
    print("COMSATS GPA Calculator")
    print()
    print("How to enter courses:")
    print("  - Enter each course as \"<course_name> <credit_hours> <gpa_recieved>\"")
    print("  - Enter \"stop\" to stop")
    print()

def enter_course(line):
    parts = line.split(' ')

    if not len(parts) == 3:
        print('Invalid input')
        return

    if not parts[0]:
        print('Invalid course_name')
        return
        
    if parts[0] in courses:
        confirm = input('course_name already exists, overwrite? (y/n): ')
        if not confirm.lower() == 'y': return

    if parts[1] not in ['0', '1', '2', '3', '4']:
        print('Invalid credit_hours')
        return
        
    if parts[2] not in ['0', '1', '1.33', '1.66', '2', '2.33', '2.66', '3', '3.33', '3.66', '4']:
        print('Invalid gpa_recieved')
    
    courses[parts[0]] = [int(parts[1]), float(parts[2])]

def calculate_cgpa():
    total_score = 0
    total_credits = 0

    for c in courses.values():
        total_score += c[0] * c[1]
        total_credits += c[1]

    cgpa = total_score / total_credits
    print('CGPA:', cgpa)

def save_courses():
    with open('courses.json', 'w') as file:
        json.dump(courses, file)

def list_courses():
    for name, values in courses.items():
        print(f"{name}: {values}")

def load_courses():
    global courses
    with open('courses.json') as file:
        courses = json.load(file)

if __name__ == '__main__':
    courses = {}
    welcome_message()

    while True:
        cmd = input('> ').strip()

        if cmd == 'exit': exit()
        elif cmd == 'list': list_courses()
        elif cmd == 'load': load_courses()
        elif cmd == 'save': save_courses()
        elif cmd == 'calc': calculate_cgpa()
        else: enter_course(cmd)
