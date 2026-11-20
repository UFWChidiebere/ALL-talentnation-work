'''STEP 1: Define a helper function to calculate the average score manually.
        - Create a variable 'total' starting at 0.
        - Create a variable 'count' starting at 0.
        - Loop through each score in the list:
            - Add the score to 'total'.
            - Add 1 to 'count'.
        - If count is greater than 0, return (total divided by count). Otherwise, return 0.

STEP 2: Define a pure function 'grade_for(avg)' to determine the letter grade.
        - Look at the grading scale using if/elif statements:
            - If avg is between 70 and 100, return 'A'
            - If avg is between 60 and 69, return 'B'
            - If avg is between 50 and 59, return 'C'
            - If avg is between 45 and 49, return 'D'
            - If avg is between 40 and 44, return 'E'
            - Otherwise, return 'F'

STEP 3: Define a process function to combine Step 1 and Step 2 for a single student.
        - Take a student dictionary.
        - Call the manual average function on their scores.
        - Call the grade function on that average.
        - Return a tuple: (student's name, their average, their grade).

STEP 4: Use 'map' to pass ALL students through the process function at once.
        - Convert the map object into a standard list.

STEP 5: Use 'filter' to extract only the passing students (Grades A, B, or C).
        - Check if the grade in the tuple is 'A', 'B', or 'C'.
        - Convert the filter object into a standard list.

STEP 6: Initialize tracking variables for Highest and Lowest students.
        - Set 'highest_student' to None and 'highest_avg' to -1 (very low default).
        - Set 'lowest_student' to None and 'lowest_avg' to 101 (very high default).

STEP 7: Loop through your mapped list of processed student tuples:
        - Print the student's name, average, and grade.
        - Check if their average is greater than 'highest_avg':
            - If yes, update 'highest_avg' and save this student's data.
        - Check if their average is lower than 'lowest_avg':
            - If yes, update 'lowest_avg' and save this student's data.

STEP 8: Print out the final summary for the highest and lowest performing students.
'''

# The raw student data structure provided by the problem
students = [
    {"name": "Sam", "scores": [80, 90]},
    {"name": "David", "scores": [55, 60]},
    {"name": "Amaka", "scores": [75, 85]},
    {"name": "Tunde", "scores": [40, 42]}
]

# --- STEP 1: Manual Average Calculator ---
def calculate_average(scores: list) -> float:
    """Calculates average manually without using sum() or len() shortcuts."""
    total = 0
    count = 0
    for score in scores:
        total += score
        count += 1
    
    if count > 0:
        return total / count
    else:
        return 0.0

# --- STEP 2: Pure Grade Assigner ---
def grade_for(avg: float) -> str:
    """Pure function that converts an average score into a letter grade."""
    if 70 <= avg <= 100:
        return 'A'
    elif 60 <= avg < 70:
        return 'B'
    elif 50 <= avg < 60:
        return 'C'
    elif 45 <= avg < 50:
        return 'D'
    elif 40 <= avg < 45:
        return 'E'
    else:
        return 'F'

# --- STEP 3: Single Student Processor ---
def process_student(student: dict) -> tuple:
    """Transforms a single student dictionary into a clean (name, average, grade) tuple."""
    avg = calculate_average(student["scores"])
    grade = grade_for(avg)
    return (student["name"], avg, grade)


# --- STEP 4: Using Map to Process All Records ---
student_profiles = list(map(process_student, students))


# --- STEP 5: Using Filter to Catch Passing Students ---
def is_passing(profile: tuple) -> bool:
    """Helper function for filter. Returns True if the grade is A, B, or C."""
    grade = profile[2] # The grade lives at index 2 of our tuple
    return grade == 'A' or grade == 'B' or grade == 'C'

passing_students = list(filter(is_passing, student_profiles))


# --- STEP 6 & 7: Loop, Track Extremes Manually, and Print ---
highest_student = None
highest_avg = -1.0 

lowest_student = None
lowest_avg = 101.0

print("--- Individual Student Reports ---")
for name, avg, grade in student_profiles:
    print(f"{name} → Average: {avg:.2f} → Grade: {grade}")
    
    # Manual check for highest performer (No max() allowed!)
    if avg > highest_avg:
        highest_avg = avg
        highest_student = (name, avg, grade)
        
    # Manual check for lowest performer (No min() allowed!)
    if avg < lowest_avg:
        lowest_avg = avg
        lowest_student = (name, avg, grade)


# --- STEP 8: Final Summary Output ---
print("\n--- Summary Performance ---")
if highest_student:
    print(f"Highest Performer: {highest_student[0]} with an average of {highest_student[1]:.2f} ({highest_student[2]})")
if lowest_student:
    print(f"Lowest Performer: {lowest_student[0]} with an average of {lowest_student[1]:.2f} ({lowest_student[2]})")



'''BONUS QUESTION ANSWER FOR QUESTION 2'''
'''IF YOU WANT TO REPLACE THE map CALL WITH A LIST COMPREHENSION, it looks like this '''
# Bonus Alternative to Step 4
student_profiles_comprehension = [process_student(s) for s in students]
