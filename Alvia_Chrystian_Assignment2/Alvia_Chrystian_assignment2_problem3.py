assignment1 = float(input("Enter the grade for Assignment 1:\t"))
assignment2 = float(input("Enter the grade for Assignment 2:\t"))
assignment3 = float(input("Enter the grade for Assignemnt 3:\t"))
quizes = float(input("Enter the grade for the Weekly Quizes:\t"))
midterm = float(input("Enter the grade for the Midterm Exam:\t"))
final = float(input("Enter the grade for the Final Exam:\t"))

assignmentAvg = ((assignment1 + assignment2 + assignment3)/3) * .25
quizAvg = (quizes * .05)
midtermAvg = (midterm * .25)
finalAvg = (final * .45)

finalGrade = (assignmentAvg + quizAvg + midtermAvg +finalAvg)/100
finalGrade = finalGrade * 100

print("\nFinal Grade:\t",format(finalGrade,"0.1f"))

if finalGrade >= 95:
    print("Is an A?\t", "True")
else:
    print("Is an A?\t", "False")


