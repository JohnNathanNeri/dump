ListOfGrades = []
PassedStudents = 0

#calculation
for num in range (5):
   x = int(input("Enter the grase of the student: "))
   if x < 40 or x > 100:
       break
   else:
       ListOfGrades.append(x)
       if x >= 75:
           PassedStudents += 1
sum = (ListOfGrades[0]) + (ListOfGrades[1]) + (ListOfGrades[2]) + (ListOfGrades[3]) + (ListOfGrades[4])
average = sum/5
passersPercintage= PassedStudents/5 * 100
print(f"Total avarage of students: {average}")
print(f"Passers: {PassedStudents}")
print(f"% {passersPercintage}")
print(f"Grades:  {ListOfGrades}")
