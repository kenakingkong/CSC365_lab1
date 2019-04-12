import pandas as pd
import sys
import numpy as np

# switch statement because they don't have one
def switch(input, students_table):

    if (input[0] == "s" or input[0] == "student"):
        if (len(input) == 3 and (input[2] == "b" or input[2]=="bus")):
            student(input[1], True, students_table);
        else:
            student(input[1],False, students_table);
    elif (input[0] == "g" or input[0]=="grade"):
        if (len(input) == 3):
            if (input[2] == "h" or input[2]=="high"):
                grade(int(input[1]), "h",students_table);
            elif (input[2] == 'l' or input[2] == "low"):
                grade(int(input[1]),'l',students_table);
        else:
            grade(int(input[1]),"none", students_table)
    elif ((input[0] == "t" or input[0] == "teacher")):
        teacher(input[1],students_table);
    elif ((input[0] == "b" or input[0]=="bus")):
        bus(int(input[1]),students_table);
    elif (input[0] == 'a' or input[0]=="average"):
        average(int(input[1]),students_table);
    elif (input[0]=='i' or input[0]=="info"):
        info(students_table);
    elif (input[0] == 'q' or input[0] == 'quit'):
        sys.exit();
    else :
        print ("Usage: F[lag]: <input> [F[lag]]");
    print("")
    main()


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
# Takes in grade number and -1, 0, or 1 to indicate if "high", "low" or
# no option was set.  If no option set, the first and last names of every
# student in the given grade level is printed.  If "high" is set, information of
# student with highest GPA of given grade level is printed.  If "low" is set,
# information of student with lowest GPA of grade is printed.
def grade(level, option, students_table):
    student_list = students_table.loc[students_table["Grade"] == level]
    if (student_list.empty):
        print("Grade Not Found");
        return;

    if(option == "none"):
        print(student_list[["StLastName", "StFirstName"]])
    else:
        if(option == "l"):
            student = students_table.iloc[student_list['GPA'].idxmin()]
        elif(option == "h"):
            student = students_table.iloc[student_list['GPA'].idxmax()]
        print(student)

# number ->
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

#main driver
def main():
    # read in text file into dataframe
    file = "students.txt";
    cols = ["StLastName","StFirstName","Grade","Classroom","Bus","GPA","TLastName","TFirstName"];
    students_table = pd.read_csv(file, sep=",",header=None, names=cols);
    #print(students_table)

    # command line prompt
    response = input("Search: ").lower().split();

    if (len(response) > 3 or len(response) < 1):
        print ("Usage: F[lag]: <input> [F[lag]]");
    else :
        switch(response, students_table);

if __name__== "__main__":
  main()
