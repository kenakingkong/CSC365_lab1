import pandas as pd
import sys

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
        else
            grade(int(input[1]),"none")
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


# String, boolean ->
# given a student lastname and option for bus, print student name
# if bus option is set, print student bus, else print grade and classroom
def student(lastname, bus, students_table):

    student_list = students_table.loc[students_table["StLastName"] == lastname.upper()]
    if(bus):
        print(student_list[["StLastName", "StFirstName","Bus"]])
    else:
        print(student_list[["StLastName", "StFirstName", "Grade", "Classroom"]])


# Search entries by teacher last name
# print the last and the first name of the student.
def teacher(teacher):

    # filters the dataframe by students with teacher last name
    student_list = students_table.loc[students_table["TLastName"] == teacher];

    # prints only these two columns
    print(student_list[["StLastName","StFirstName"]])


# find the bus route with matching number
# output the student first and last name, grade and Classroom
def bus(route):

    student_list = students_table.loc[students_table["Bus"]]
    print(student_list[["SFirstName","SLastName","Grade","Classroom"]])

# find the matching grade (within constraints if given)
#



# String, boolean ->
# given a student lastname and option for bus, print student name
# if bus option is set, also print student bus, else print grade and classroom
def student(lastname, bus=false):
    student_list = students_table[students_table["StLastName"] == lastname]
    if(bus):
        print(student_list[[StLastName, StFirstName, Bus]])
    else:
        print(student_list[[StLastName, StFirstName, Grade, Classroom, TLastName, TFirstName]])

def main():
    # read in text file into dataframe
    file = "students.txt";
    cols = ["StLastName","StFirstName","Grade","Classroom","Bus","GPA","TLastName","TFirstName"];
    students_table = pd.read_csv(file, sep=",",header=None, names=cols);
    #print(students_table)

    # command line prompt
    response = input("Search: ").lower().split();

    if (len(input) < 2 or len(input) > 3):
        print ("Usage: F[lag]: <input> [F[lag]]");
    else :
        switch(response, students_table);


def grade(num):
    student_list = students_table[students_table["Grade"] == grade]
    print(student_list[[StLastName, StFirstName, ]])



if __name__== "__main__":
  main()
