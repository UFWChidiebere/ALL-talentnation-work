def calculate_grades(students):

    highest_avg = -1.0
    lowest_avg = 101.0
    highest_student = ""
    lowest_student = ""

    for student in students:
        name = student["name"]
        scores = student["scores"]

        '''manual sum calculation'''
        total_score = 0
        count = 0

        for score in scores:
            total_score += score
            count += 1

        average = total_score / count if count > 0 else 0
        if average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 45:
            grade = "D"
        elif average >= 40:
            grade = "E"
        else:
            grade = "F"

        print(f"{name} -> Average: {average:.2f} -> Grade: {grade}")



        """tracking highest and lowest performance namnually"""
        if  average > highest_avg:
            highest_avg = average
            highest_student = name

        if average < lowest_avg:
            lowest_avg = average
            lowest_student = name

    print(f"\nHighest Performing Student: {highest_student} ({highest_avg:.2f})")
    print(f"Lowest Performing Student: {lowest_student} ({lowest_avg:.2f})")

students = [{"name": "Sam", "scores": [80, 90]}, {"name": "David", "scores": [55, 60]}]
calculate_grades(students)













"""Initialize Extremes: Set highest_avg = -1 and lowest_avg = 101. Keep string trackers for highest_student and lowest_student.

    Loop and Manual Sum: Iterate through each student dictionary. To get the average without sum(), use a for loop to accumulate scores and divide by the loop count.

    Map Grade: Use conditional chains (if/elif) matching the specific 40-70 scaling brackets to isolate the correct letter grade.
    
    Track Leaderboard: Compare the calculated average against highest_avg and lowest_avg. Overwrite if a new extreme is found."""
