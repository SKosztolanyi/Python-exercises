class Grades(object):
    ''' A mapping from students to a list of grades'''
    def __init__(self):
        '''Create an empty grade book'''
        self.students = [] # Creates a list of Student objects
        self.grades = {} # Maps idNum -> list of grades (into dictionary)
        self.isSorted = True #true if self.students is sorted
        
    def addStudent(self, student):
        '''Assumes: student is of type Student
        add a student to the grade book'''
        if student in self.students:
            raise ValueError("Duplicate Student")
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False
        
    def addGrade(self, student, grade):
        '''Assumes: grade is a float
        Student is in a list
        Add grade to the list of grades for student'''
        try:
            self.grades[student.getIdNum()].append(grade)
        except KeyError:
            raise ValueError("Student not in grade book")
            
    def getGrades(self, student):
        '''Return a list of grades for student'''
        try: # return copy of student's grades
            return self.grades[student.getIdNum()][:]
        except KeyError:
            raise ValueError("Student not in grade book")
        
    def allStudents(self):
        '''Return a list of all the students in the grade book'''
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:]
        # return a copy of list of students
        
        
def gradeReport(course): 
    # This is not a method of a class Grades, but a function that operates on that class without need for internal details.
    '''Assumes: course is of type grades'''
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot/numGrades
            report.append(str(s) + "\"s mean grade is" + str(average))
        except ZeroDivisionError:
            report.append(str(s) + "has no grades")
        return "\n".join(report)