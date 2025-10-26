#A brief message about the project
print("CODE THE VACATION WITH MORTOTI CHALLENGE 2025")
print("PROJECT AUTHOR: Isaac Atoeyine Anafo")
print("PROJECT TITLE: GradeMaster, academic Performance Evaluation Tool")
print("PROJECT DESCRIPTION: This program calculates students' CWA or GPA based on their course inputs.")
def welcome_student():
    """
    Ask for the user's name and institution name.
    Display a welcome message and brief instructions about the program.
    Returns:
        The student's full name.
        The name of the student's institution.
    """
    student_name = input("Please enter your full name: ").strip().title()
    institution_name = input("\nPlease enter your institution (School) name: ").strip().title()
    print(f"\nWelcome, {student_name}, to GradeMaster!")
    print("This program helps you calculate and evaluate your academic performance.")
    print("You'll be asked to enter your school's grading system (CWA or GPA), course names, credit hours, and exam marks or grades.")
    print("The program then proficiently calculates your CWA or GPA, and goes ahead to evaluate it, all within a second.")
    print("An academic report is then displayed to you for your convenient keep.")
    print("Just make sure your inputs are valid and you do follow the prompts carefully!\n")
    return student_name, institution_name

def get_grading_system():
    """
    Prompt the user to input the grading system used by their school.
    Continues to ask until a valid input ('CWA' or 'GPA') is provided.
    Returns:
        The validated grading system, either 'CWA' or 'GPA'.
    """
    while True:
        system = input("What grading system does your school use? (CWA/GPA): ").strip().upper()
        if system in ['CWA', 'GPA']:
            return system
        else:
            print("\nInvalid input. Enter a correct grading system.")

            
def get_course_data(system):
    """
    Ask for course details such as number of courses, course names,
    credit hours, and either marks (for CWA) or grades (for GPA).
    Calculate and return the total weight or points and total credit hours
    for performance evaluation.
    Returns:
        Either total_weight and total_credit_hours for CWA calculation or
        total_points and total_credit_hours for GPA calculation.
    """
    total_weight = 0
    total_points = 0
    total_credit_hours = 0
    while True:
        number_of_courses = int(input("\nEnter the total number of courses you are offering (Must be greater than zero): "))
        if number_of_courses > 0:
            break
        else:
            print("\nInvalid input. Number of courses must be greater than 0.")
    for i in range(1, number_of_courses + 1):
        course_name = input(f"\nEnter the name of course {i}: ")
        while True:
            credit = int(input("\nEnter the credit hours for this course (Must be greater than zero): "))
            if credit > 0:
                break
            else:
                print("\nInvalid input. Credit hours must be greater than 0.")

        if system == 'CWA':
            while True:
                mark = float(input("\nEnter the exam mark for this course (0 - 100): "))
                if 0 <= mark <= 100:
                    break
                else:
                    print("\nInvalid mark. Must be between 0 and 100.")
            total_weight += mark * credit
        else:
            while True:
                grade = input("\nEnter the grade for this course (A/B/C/D/E/F): ").strip().upper()
                if grade in ['A', 'B', 'C', 'D', 'E', 'F']:
                    break
                else:
                    print("\nInvalid grade. Please enter A, B, C, D, E, or F.")
            if grade == 'A':
                point = 4.0
            elif grade == 'B':
                point = 3.0
            elif grade == 'C':
                point = 2.0
            elif grade == 'D':
                point = 1.0
            elif grade == 'E':
                point = 0.5
            else:  # F
                point = 0.0
            total_points += point * credit
        total_credit_hours += credit
    if system == 'CWA':
        return total_weight, total_credit_hours
    else:
        return total_points, total_credit_hours