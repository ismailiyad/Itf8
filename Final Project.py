import sys
from student import Student
from course import Course
students = []

while True:
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark\n"
                              "6.Exit: "))

        def add_student():
            student_number = input("Enter Student Number: ")
            student_name = input("Enter Student Name: ")
            student_age = int(input("Enter Student Age: "))
            new_student = Student(student_name, student_age, student_number)
            students.append(new_student)
            print("Student Added Successfully\n""--------------------------------")

        def delete_student():
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    students.remove(student)
                    print("Student Deleted Successfully\n""--------------------------------")
                    break
            else:
                print("Student Not Exist\n""--------------------------------")

        def display_student():
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    print(f"Student Name: {student.student_name}")
                    print(f"Student Age: {student.student_age}")
                    print("Courses:")
                    if len(student.courses_list) > 0:
                        for course in student.courses_list:
                            print(f"Course: {course.course_name}, Mark: {course.course_mark}")
                        print("---------------------------------")
                    else:
                        print("No courses registered.\n" "--------------------------------")
                    break
            else:
                print("Student Not Exist\n" "--------------------------------")

        def get_student_average():
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    average = student.get_student_average()
                    print(f"Student Average: {average}")
                    break
            else:
                print("Student Not Exist\n""--------------------------------")

        def add_course():
            student_number = input("Enter Student Number: ")
            for student in students:
                if student.student_number == student_number:
                    course_name = input("Enter Course Name: ")
                    course_mark = float(input("Enter Course Mark: "))
                    new_course = Course(course_name, course_mark)
                    student.enroll_course(new_course)
                    print("Course Added Successfully\n""--------------------------------")
                    break
            else:
                print("Student Not Exist")

        def exit_program():
            exit()

        switch = {
            1: add_student,
            2: delete_student,
            3: display_student,
            4: get_student_average,
            5: add_course,
            6: exit_program
        }

        switch.get(selection, lambda: print("Invalid Input"))()

    except ValueError:
        print("Invalid Input")
