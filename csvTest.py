import csv


def idGen(student):
    studentid = {"Chang, Stephanie": "20140800050", "Chen, Cici": "20120700011", "Chiang, Darren": "20070200002",
                 "Ho, Sabrina": "20141000057", "Huang, Daniel": "20140900054", "Tai, Alex": "20120800023"}
    return studentid[student]


def convert1(filename):
    # Template of pwrskl file
    data = [("Teacher Name: ", "Ruben Dario Pinon Morales"), ("Section: ", "Python")]
    data2 = [("Points Possible: ", "10", ""), ("Extra Points: ", "0", ""), ("Score Type: ", "Points", ""),
             ("Score Type: ", "Points", ""), ("Student ID", "Student Name", "Points")]

    # Opening google file for reading
    google = open("GoogleActivities.csv")
    reader = csv.reader(google)

    # Taking values of google file and reformatting it into data variable
    for idj, row in enumerate(reader):
        for idx, column in enumerate(row):
            if column == "Email Address":
                assignmentName = row[idx+1]
            elif column == "Date":
                dueDate = row[idx+3]

        if idj == 3:
            student1 = row[1] + ", " + row[0]
            points = int(row[3])/10
        elif idj == 4:
            student2 = row[1] + ", " + row[0]
            points = int(row[3])/10
        elif idj == 5:
            student3 = row[1] + ", " + row[0]
            points = int(row[3])/10
        elif idj == 6:
            student4 = row[1] + ", " + row[0]
            points = int(row[3])/10
        elif idj == 7:
            student5 = row[1] + ", " + row[0]
            points = int(row[3])/10
        elif idj == 8:
            student6 = row[1] + ", " + row[0]
            points = int(row[3])/10

    data.append(("Assignment Name: ", assignmentName))
    data.append(("Due Date: ", dueDate))

    for row in data2:
        data.append(row)

    grades = [(idGen(student1), student1, points), (idGen(student2), student2, points),
              (idGen(student3), student3, points), (idGen(student4), student4, points),
              (idGen(student5), student5, points), (idGen(student6), student6, points)]
    for row in grades:
        data.append(row)

    # Creating copy file for writing the google file into pwrskl file
    copy = open(filename+".csv", "w")
    writer = csv.writer(copy, delimiter=",")

    # Writing values of data into copy file
    for values in data:
        writer.writerow(values)

    google.close()
    copy.close()


def convert2(filename):
    # Template of pwrskl file
    data = [("Teacher Name: ", "Ruben Dario Pinon Morales"), ("Section: ", "Python")]
    data2 = [("Points Possible: ", "10", ""), ("Extra Points: ", "0", ""), ("Score Type: ", "Points", ""),
             ("Score Type: ", "Points", ""), ("Student ID", "Student Name", "Points")]

    # Opening google file for reading
    google = open("GoogleActivities.csv")
    reader = csv.reader(google)



    # Taking values of google file and reformatting it into data variable
    for idj, row in enumerate(reader):
        for idx, column in enumerate(row):
            if column == "Email Address":
                assignmentName = row[idx+2]
            elif column == "Date":
                dueDate = row[idx+4]

        if idj == 3:
            student1 = row[1] + ", " + row[0]
            points = int(row[4])/10
        elif idj == 4:
            student2 = row[1] + ", " + row[0]
            points = int(row[4])/10
        elif idj == 5:
            student3 = row[1] + ", " + row[0]
            points = int(row[4])/10
        elif idj == 6:
            student4 = row[1] + ", " + row[0]
            points = int(row[4])/10
        elif idj == 7:
            student5 = row[1] + ", " + row[0]
            points = int(row[4])/10
        elif idj == 8:
            student6 = row[1] + ", " + row[0]
            points = int(row[4])/10

    data.append(("Assignment Name: ", assignmentName))
    data.append(("Due Date: ", dueDate))

    for row in data2:
        data.append(row)

    grades = [(idGen(student1), student1, points), (idGen(student2), student2, points),
              (idGen(student3), student3, points), (idGen(student4), student4, points),
              (idGen(student5), student5, points), (idGen(student6), student6, points)]
    for row in grades:
        data.append(row)




    # Creating copy file for writing the google file into pwrskl file
    copy = open(filename+".csv", "w")
    writer = csv.writer(copy, delimiter=",")

    # Writing values of data into copy file
    for values in data:
        writer.writerow(values)

    google.close()
    copy.close()


def convert3(filename):
    # Template of pwrskl file
    data = [("Teacher Name: ", "Ruben Dario Pinon Morales"), ("Section: ", "Python")]
    data2 = [("Points Possible: ", "10", ""), ("Extra Points: ", "0", ""), ("Score Type: ", "Points", ""),
             ("Score Type: ", "Points", ""), ("Student ID", "Student Name", "Points")]

    # Opening google file for reading
    google = open("GoogleActivities.csv")
    reader = csv.reader(google)



    # Taking values of google file and reformatting it into data variable
    for idj, row in enumerate(reader):
        for idx, column in enumerate(row):
            if column == "Email Address":
                assignmentName = row[idx+3]
            elif column == "Date":
                dueDate = row[idx+5]

        if idj == 3:
            student1 = row[1] + ", " + row[0]
            points = int(row[5])/10
        elif idj == 4:
            student2 = row[1] + ", " + row[0]
            points = int(row[5])/10
        elif idj == 5:
            student3 = row[1] + ", " + row[0]
            points = int(row[5])/10
        elif idj == 6:
            student4 = row[1] + ", " + row[0]
            points = int(row[5])/10
        elif idj == 7:
            student5 = row[1] + ", " + row[0]
            points = int(row[5])/10
        elif idj == 8:
            student6 = row[1] + ", " + row[0]
            points = int(row[5])/10

    data.append(("Assignment Name: ", assignmentName))
    data.append(("Due Date: ", dueDate))

    for row in data2:
        data.append(row)

    grades = [(idGen(student1), student1, points), (idGen(student2), student2, points),
              (idGen(student3), student3, points), (idGen(student4), student4, points),
              (idGen(student5), student5, points), (idGen(student6), student6, points)]
    for row in grades:
        data.append(row)




    # Creating copy file for writing the google file into pwrskl file
    copy = open(filename+".csv", "w")
    writer = csv.writer(copy, delimiter=",")

    # Writing values of data into copy file
    for values in data:
        writer.writerow(values)

    google.close()
    copy.close()


def convert4(filename):
    # Template of pwrskl file
    data = [("Teacher Name: ", "Ruben Dario Pinon Morales"), ("Section: ", "Python")]
    data2 = [("Points Possible: ", "10", ""), ("Extra Points: ", "0", ""), ("Score Type: ", "Points", ""),
             ("Score Type: ", "Points", ""), ("Student ID", "Student Name", "Points")]

    # Opening google file for reading
    google = open("GoogleActivities.csv")
    reader = csv.reader(google)



    # Taking values of google file and reformatting it into data variable
    for idj, row in enumerate(reader):
        for idx, column in enumerate(row):
            if column == "Email Address":
                assignmentName = row[idx+4]
            elif column == "Date":
                dueDate = row[idx+6]

        if idj == 3:
            student1 = row[1] + ", " + row[0]
            points = int(row[6])/10
        elif idj == 4:
            student2 = row[1] + ", " + row[0]
            points = int(row[6])/10
        elif idj == 5:
            student3 = row[1] + ", " + row[0]
            points = int(row[6])/10
        elif idj == 6:
            student4 = row[1] + ", " + row[0]
            points = int(row[6])/10
        elif idj == 7:
            student5 = row[1] + ", " + row[0]
            points = int(row[6])/10
        elif idj == 8:
            student6 = row[1] + ", " + row[0]
            points = int(row[6])/10

    data.append(("Assignment Name: ", assignmentName))
    data.append(("Due Date: ", dueDate))

    for row in data2:
        data.append(row)

    grades = [(idGen(student1), student1, points), (idGen(student2), student2, points),
              (idGen(student3), student3, points), (idGen(student4), student4, points),
              (idGen(student5), student5, points), (idGen(student6), student6, points)]
    for row in grades:
        data.append(row)




    # Creating copy file for writing the google file into pwrskl file
    copy = open(filename+".csv", "w")
    writer = csv.writer(copy, delimiter=",")

    # Writing values of data into copy file
    for values in data:
        writer.writerow(values)

    google.close()
    copy.close()


def mainConvert(filename1, filename2, filename3, filename4):
    convert1(filename1)
    convert2(filename2)
    convert3(filename3)
    convert4(filename4)

mainConvert("Assignment 1", "Assignment 2", "Assignment 3", "Assignment 4")
