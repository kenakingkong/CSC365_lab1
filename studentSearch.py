import pandas as pd
import sys

# put each function

def main():

    # read in text file into dataframe
    file = "students.txt";
    students_table = pd.read_csv(file, sep=" ");

    # command line prompt
    response = input("Search: ")

    # switch and call each function
    switch(response) {
        case "S":
            #S[tudent]: <lastname> [B[us]]
            break;

        case "T":
            #T[eacher]: <lastname>
            break;

        case "B":
            # B[us]: <number>
            break;

        case "G":
            #G[rade]: <number> [H[eight]|L[ow]]
            break;

        case "A":
            #A[verage]: <number>

        case "I":
            #I[nfo]

        case "Q":
            #Q[uit]
            # sys.exit?
            break;

        default:
            #print error statement
            print ("Usage: F[lag]: <input> [F[lag]]")
            break
    }



# String, boolean ->
# given a student lastname and option for bus, print student name
# if bus option is set, also print student bus, else print grade and classroom
def student(lastname, bus=false):
    student_list = students_table[students_table["StLastName"] == lastname]
    if(bus):
        print(student_list[[StLastName, StFirstName, Bus]])
    else:
        print(student_list[[StLastName, StFirstName, Grade, Classroom, TLastName, TFirstName]])


# Search entries by teacher last name
# print the last and the first name of the student.
def teacher(teacher):

    # filters the dataframe by students with teacher last name
    student_list = students_table[students_table["TLastName"] == teacher]

    # prints only these two columns
    print(student_list[[StLastName,StFirstName]])

def grade(num):
    student_list = students_table[students_table["Grade"] == grade]
    print(student_list[[StLastName, StFirstName, ]])



if __name__== "__main__":
  main()
