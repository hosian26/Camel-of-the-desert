 CGPA cheaking

 def calculate_cgpa():

     grade_points_map = {
         'A+': 4.0,
         'A': 3.7,
         'B+': 3.3,
         'B': 3.0,
         'C+': 2.5,
         'C': 2.0,
         'D': 1.0,
         'F': 0.0
     }

     total_grade_points = 0
     num_subjects = int(input("Enter the number of subjects: "))

     def get_grade_point(marks):
         if 80 <= marks <= 100:
             return grade_points_map['A+']
         elif 75 <= marks <= 79:
             return grade_points_map['A']
         elif 70 <= marks <= 74:
             return grade_points_map['A-']
         elif 65 <= marks <= 69:
             return grade_points_map['B+']
         elif 60 <= marks <= 64:
             return grade_points_map['B']
         elif 55 <= marks <= 59:
             return grade_points_map['B-']
         elif 50 <= marks <= 54:
             return grade_points_map['C+']
         elif 45 <= marks <= 49:
             return grade_points_map['C']
         elif 40 <= marks <= 44:
             return grade_points_map['D']
         else:
             return grade_points_map['F']

     for i in range(num_subjects):
         mark = float(input(f"Enter the marks for subject {i + 1}: "))
         grade_point = get_grade_point(mark)
         total_grade_points += grade_point

     gpa = total_grade_points / num_subjects
     print("Your CGPA is: ", round(gpa, 2))
 calculate_cgpa()
 from itertools import count
















