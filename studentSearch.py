import pandas as pd
import sys
import numpy as np

# pass input into switch
def get_user_input(students_table, teachers_table):
    # command line prompt
    response = input("Search: ").lower().split();

    if (len(response) > 3 or len(response) < 1):
        print ("Usage: F[lag]: <input> [F[lag]]");
    else :
        switch(response, students_table, teachers_table);

# new commands:
# C[lass] <class #> S[tudent]|T[eacher]
# G[rade] <grade #> [S[tudent] [[H]igh|[L]ow]]|T[eacher]
# E[nrollment]

# switch statement because they don't have one
def switch(input, students_table, teachers_table):

    if (input[0] == "s" or input[0] == "student"):
        if (len(input) == 3 and (input[2] == "b" or input[2]=="bus")):
            student(input[1], True, students_table);
        else:
            student(input[1],False, students_table);
    elif (input[0] == "g" or input[0]=="grade"):
        if (len(input) == 4):
            if (input[3] == "h" or input[3]=="high"):
                grade(int(input[1]), "h",students_table);
            elif (input[3] == 'l' or input[3] == "low"):
                grade(int(input[1]),'l',students_table);
        else:
            if(input[2] == 's' or input[2] == 'students'):
                grade(int(input[1]),"none", students_table, teachers_table)
            elif(input[2] == 't' or input[2] == 'teachers'):
                grade(int(input[1]), "none", students_table, teachers_table, True)
    elif ((input[0] == "t" or input[0] == "teacher")):
        teacher(input[1],students_table);
    elif ((input[0] == "b" or input[0]=="bus")):
        bus(int(input[1]),students_table);
    elif (input[0] == 'a' or input[0]=="average"):
        average(int(input[1]),students_table);
    elif (input[0]=='i' or input[0]=="info"):
        info(students_table);
    elif (input[0]=='c' or input[0]=="class"):
        if (len(input) == 3):
            if (input[2]=="s" or input[2]=="student"):
                classroom(int(input[1]), 's', students_table);
            elif (input[2]=="t" or input[2]=="teacher"):
                classroom(int(input[2]), 't', students_table, teachers_table);
        else:
            print ("Usage: F[lag]: <input> [F[lag]]");
    elif (input[0]=='e' or input[0]=="enrollment"):
        enrollment(students_table)
    elif (input[0]=="analytics"):
        get_analytics_input(students_table, teachers_table);
    elif (input[0] == 'q' or input[0] == 'quit'):
        sys.exit();
    else :
        print ("Usage: F[lag]: <input> [F[lag]]");

    print("")

    # reprompt until quit
    get_user_input(students_table, teachers_table);


# String, boolean ->
# given a student lastname and option for bus, print student name
# if bus option is set, print student bus, else print grade and classroom
def student(lastname, bus, students_table):

    student_list = students_table.loc[students_table["StLastName"] == lastname.upper()];
    if (student_list.empty):
        print("Student not found");
        return;

    if(bus):
        print(student_list[["StLastName", "StFirstName","Bus"]])
    else:
        print(student_list[["StLastName", "StFirstName", "Grade", "Classroom"]])


# Search entries by teacher last name
# print the last and the first name of the student.
def teacher(teacher, students_table):

    # filters the dataframe by students with teacher last name
    student_list = students_table.loc[students_table["TLastName"] == teacher.upper()];
    if (student_list.empty):
        print("Teacher not found");
        return;

    # prints only these two columns
    print(student_list[["StLastName","StFirstName"]].to_string(index=False))


# find the bus route with matching number
# output the student first and last name, grade and Classroom
def bus(route, students_table):

    student_list = students_table.loc[students_table["Bus"] == route];
    if (student_list.empty):
        print("Bus Route not found");
        return;

    print(student_list[["StFirstName","StLastName","Grade","Classroom"]])

# number, number ->
# Takes in grade number and "high", "low", or "none" if no option was set.
# If no option set, the first and last names of every
# student in the given grade level is printed.  If "high" is set, information of
# student with highest GPA of given grade level is printed.  If "low" is set,
# information of student with lowest GPA of grade is printed.
def grade(level, h_l, student_table, teacher_table, teacher=False):
    student_list = student_table.loc[student_table["Grade"] == level]
    if (student_list.empty):
        print("Grade Not Found");
        return;
    if(teacher):
        class_list = student_list.Classroom.unique()
        teacher_list = teacher_table.loc[teacher_table["Classroom"].isin(class_list)]
        print(teacher_list[["TLastName", "TFirstName"]])
    else:
        if(h_l == "none"):
            print(given_list[["StLastName", "StFirstName"]])
        else:
            if(option == "l"):
                student = student_table.iloc[student_list['GPA'].idxmin()]
            elif(option == "h"):
                student = student_table.iloc[student_list['GPA'].idxmax()]
            print(student)

# given a grade level, takes all of the GPAs for that grade and prints the average
def average(grade, students_table):
    GPA_list = students_table.loc[students_table["Grade"] == grade, ['GPA']]
    if (GPA_list.empty):
        print("Grade not found");
        return;
    print('{}, {}'.format(grade, round(GPA_list.sum().get(0)/GPA_list.size, 2)))

# ->
# prints each grade level and corresponding number of students in the grade level
def info(students_table):
    student_list = students_table["Grade"]
    if (student_list.empty):
        print("Info not found");
        return;

    print(student_list.value_counts().sort_index().to_frame())

# list students or teachers by classroom number
def classroom(room, option, table):

    new_list = table.loc[table["Classroom"] == room];
    if (new_list.empty):
        print("Classroom not found");
    else :
        if (option == "s"): #table = students_table
            print(new_list[["StLastName", "StFirstName"]]);
        elif (option == "t"): # table = teacher_table
            print(new_list[["TLastName","TFirstName"]]);
        else :
            print ("Usage: F[lag]: <input> [F[lag]]");


# dataframe -> print out list of classroom, ordered by number, with each
# classroom's enrollment
def enrollment(students_table):
    class_list = students_table["Classroom"]
    if (class_list.empty):
        print("No classrooms in system")
        return
    print(class_list.value_counts().sort_index().to_frame())



''' ANALYTICS PORTION '''

# pass analytics input into switch
def get_analytics_input(students_table, teachers_table):
    print("***ANALYTICS***");
    print("Usage:");
    print("1. GPA G|T|B <input>\n   Get the Average GPA by Grade, Teacher or Bus Route")
    print("2. GPA all G|T|B [G|T|B] \n   Get Average GPAs by Grade, Teacher or Bus Route optionally sorted by Grade Teacher or Bus, Route");
    print("3. GPA all \n   Get all GPAs sorted by Grade, Teacher or Bus Route")
    response = input("Search: ").lower().split();

    if (len(response) > 4 or len(response) < 2):
        print ("Usage: GPA F[lag]: <input> [F[lag]]");
    else :
        # pass in input without "GPA"
        analytics_switch(response[1:], students_table, teachers_table);

def analytics_switch(response, students_table, teachers_table):
    # currently testing the

    '''
    if (response[0] == "all"):
        if (response[1]):
            averages(-----);
        else:
            overallGPA(students_table, teachers_table);
    '''


# alter to accept grade, teacher ,bus route
# returns the average of all students in given Grade, Bus Route or Teacher
def average(column, input,  students_table):


    GPA_list = students_table.loc[students_table[calumn] == input, ['GPA']]
    if (GPA_list.empty):
        print("Grade not found");
        return;
    print('{}, {}'.format(grade, round(GPA_list.sum().get(0)/GPA_list.size, 2)))


# get average by teacher or bus routes
def averageBy(students_table, teachers_table):
    pass;

# return the average gpa of all grades, teachers OR bus routes
# optional sort by grade, teacher or bus routes
# default will be its own
def averages(students_table, teachers_table, option, sortBy):
    # sort by teachers
    if (sortBy == "t"):
        pass;

# return every single GPA
def overallGPA(students_table, teachers_table):
    pass;

#main driver
def main():

    # read in students data into data frame
    file = "list.txt";
    student_cols = ["StLastName","StFirstName","Grade","Classroom","Bus","GPA"];
    students_table = pd.read_csv(file, sep=",",header=None, names=student_cols);

    # read in teachers data into data frame
    file = "teachers.txt";
    teacher_cols =["TLastName", "TFirstName", "Classroom"];
    teachers_table = pd.read_csv(file, sep=",",header=None, names=teacher_cols)

    # prompt function
    get_user_input(students_table, teachers_table);

if __name__== "__main__":
  main()
