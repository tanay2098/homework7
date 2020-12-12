import pandas as pd
READ_FILENAME = 'scores.csv'
grade = ''
grade_score = 0.0

def student_grades(p_score):
    if p_score >= 90:
        grade = 'A'
        grade_score = 4.0
    elif p_score >= 80:
        grade = 'B'
        grade_score = 3.0
    elif p_score >= 70:
        grade = 'C'
        grade_score = 2.0
    elif p_score >= 60:
        grade = 'D'
        grade_score = 1.0
    elif p_score < 60:
        grade = 'F'
        grade_score = 0.0
    return grade_score

scores = pd.read_csv(READ_FILENAME, delimiter=',', index_col=0, header=0)

 #dataframe for grade and gpa
grades = scores.applymap(student_grades)

pd.set_option('precision', 2) #for 2 decimal places
x_mean = grades.mean(axis = 0)#individual gpa
print(x_mean)
x_gpa = grades.stack().mean()#calculate class gpa
print(f'The class GPA is {x_gpa:.2f}')
