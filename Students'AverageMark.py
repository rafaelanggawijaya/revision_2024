
def scores(best_student, average_mark, id):
    name = []
    total_marks = 0
    score = []
    id = []
    num_stundets = 0
    best_student = []
    average_mark = ""
    while True:
        student_name = input("Student's name: ").title()
        if student_name == "x" or "X":
            print("Program Ended")
            break
        else:
            name.append(student_name)
            num_students += 1
        while True:
            marks = int(input("Student's mark (0-100): "))
            if marks >= 0 and marks <= 100 :
                total_marks += marks
                score.append(marks)
                break
            else:
                print("please enter a valid score")
        id.append(student_name, marks)
        average_mark = round(total_marks / num_students,2)
        for student in id:
            if student[1] > best_student:
                best_student = student[1]
                best_student = [student]
            elif student[1] == best_student:
                best_student.append(student)

highest_score = ""
average = ""
list = ""
scores(highest_score,average,list )
print(f"The student with the highest scores is {highest_score} ")