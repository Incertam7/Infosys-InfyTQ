#PF-Tryout
#Start writing your code here
marks = 69
grade = ''

if(marks >= 80 and marks <= 100):
    grade = 'A'
elif(marks >= 73 and marks < 80):
    grade = 'B'
elif(marks >= 65 and marks < 73):
    grade = 'C'
elif(marks >= 0 and marks < 65):
    grade = 'D'
else:
    grade = 'Z'
    
print(grade)
