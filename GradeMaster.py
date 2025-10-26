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