
def student_grades(student_data_score):
    for students in student_data_score:
        name = students[0]
        avarage = round((students[1] + students[2]+ students[3])/3, 2)
        if avarage >= 70:# or avarage <= 100:
            grades = "A"
            print (f"{name} - Average: {avarage} - Grade: {grades}")
        elif avarage >= 60: #or avarage <= 69 :
            grades = "B"
            print (f"{name} - Average: {avarage} - Grade: {grades}")
        elif avarage >= 50:# or avarage <= 59:
            grades = "C"
            print (f"{name} - Average: {avarage} - Grade: {grades}")
        elif avarage >= 45 :#or avarage <= 49:
            grades = "D"
            print (f"{name} - Average: {avarage} - Grade: {grades}")
        elif avarage >= 40:# or avarage <= 39:
            grades = "E"
            print (f"{name} - Average: {avarage} - Grade: {grades}")
        elif avarage >= 0:# or avarage <= 39:
                    grades = "F"
                    print (f"{name} - Average: {avarage} - Grade: {grades}")


student_grades([
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
])


"""another approach to getting this"""
def calculate_grade(average):
    if average >= 70: return 'A'
    elif average >= 60: return 'B'
    elif average >= 50: return 'C'
    elif average >= 45: return 'D'
    elif average >= 40: return 'E'
    else: return 'F'

def process_student_grades(students):
    for student in students:
        name = student[0]
        total_score = 0
        score_count = 0
        
        # Manually track and loop scores starting from index 1
        for score in student[1:]:
            total_score += score
            score_count += 1
            
        average = total_score / score_count if score_count > 0 else 0.0
        grade = calculate_grade(average)
        print(f"{name} → Average: {average:.2f} → Grade: {grade}")

# 1. Define your data matrix (a list of lists)
student_data = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

# 2. Call the function and pass your list into it
process_student_grades(student_data)



"""another approach"""

def alternative_grades(students):
    # Custom scale tracking upper bound limit to letter grade mapping
    grade_scale = [(70, 'A'), (60, 'B'), (50, 'C'), (45, 'D'), (40, 'E'), (0, 'F')]

    for student in students:
        name, *scores = student  # Python automatically separates name string from all score integers
        
        total = 0
        for s in scores: total += s
        avg = total / len(scores)
        
        # Scan scale to find the matching bracket
        final_grade = 'F'
        for cutoff, grade in grade_scale:
            if avg >= cutoff:
                final_grade = grade
                break
                
        print(f"{name} → Average: {avg:.2f} → Grade: {final_grade}")

# 1. Define your data
student_data = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68]
]

# 2. Call the alternative function
alternative_grades(student_data)





        

        