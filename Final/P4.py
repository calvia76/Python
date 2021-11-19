student_to_grades = {}


student_to_grades["123"] = ["111","90.75"]
student_to_grades["456"] = ["111","73.23"]
student_to_grades["789"] = ["111","70.75"]

student_to_grades["123"] = ["112","83.63"]
student_to_grades["456"] = ["112","52.91"]
student_to_grades["789"] = ["112","79.29"]



student_to_grades["113"] = ["151","92.34"]
student_to_grades["112"] = ["151","60.42"]
student_to_grades["114"] = ["151", "84.23"]

student_to_grades["113"] = ["152","89.65"]
student_to_grades["112"] = ["152","95.25"]
student_to_grades["114"] = ["152","45.03"]


#def course_grader(student_to_grades, course_prefix):

x = student_to_grades["123"]
print(x[0],x[1])
