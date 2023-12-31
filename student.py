import random
class Student:
    total_students = 0

    def __init__(self, student_name, student_age, student_number):
        self.student_id = random.randint(10000, 99999)
        self.student_name = student_name
        self.student_age = student_age
        self.student_number = student_number
        self.courses_list = []

    def enroll_course(self, course):
        self.courses_list.append(course)

    def get_student_courses(self):
        for course in self.courses_list:
            print(f"Course: {course.course_name}, Mark: {course.course_mark}")

    def get_student_average(self):
        total_marks = sum(course.course_mark for course in self.courses_list)
        return total_marks / len(self.courses_list)