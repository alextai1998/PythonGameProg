"""
This program takes a google grades csv file and a template powerschool grades file, and generates several csv files
according to the number of assignments on the google csv file.
"""

import csv
import datetime

# Opens google file for reading and then stores values into a list variable
g = open("Test- GoogleClassroom.csv")
gcData = [row for row in csv.reader(g)]
g.close()

# Opens google file for reading and then stores values into a list variable
p = open("PowerSchoolTemplateRobotics_pst.csv")
psData = [row for row in csv.reader(p)]
p.close()

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "June": 6, "July": 7, "Aug": 8, "Sept": 9, "Oct": 10,
         "Nov": 11, "Dec": 12}

for A in range(len(gcData[0])-3):  # Iterates number of assignments

    monthLetter = gcData[1][3+A][3]+gcData[1][3+A][4]+gcData[1][3+A][5]
    if monthLetter == "Jun" or monthLetter == "Jul" or monthLetter == "Sep":
        monthLetter = gcData[1][3+A][3]+gcData[1][3+A][4]+gcData[1][3+A][5]+gcData[1][3+A][6]
    day = gcData[1][3+A][0]+gcData[1][3+A][1]
    year = "20" + gcData[1][3+A][-2]+gcData[1][3+A][-1]
    weekday = week[datetime.date(int(year), month[monthLetter], int(day)).weekday()]
    dueDate = weekday + " " + monthLetter + " " + day + " 00:00:00 CST " + year

    data = [("Teacher Name: ", psData[0][1]), ("Section: ", psData[1][1]), ("Assignment Name: ", gcData[0][3+A]),
            ("Due Date: ", dueDate), ("Points Possible: ", "10", ""), ("Extra Points: ", "0", ""),
            ("Score Type: ", "Points", ""), ("Student ID", "Student Name", "Points")]

    for S in range(len(psData)-9):  # Iterates number of students
        studentid = {}
        studentid[psData[9+S][1]] = psData[9+S][0]  # Generates dictionary of student IDs from PS file
        studentName = gcData[3+S][1] + ", " + gcData[3+S][0]
        points = int(gcData[3+S][3+A])/10
        data.append((studentid[studentName], studentName, points))  # Matches GC file names with PS file IDs

    # Creates powerschool file from google file data
    a = open("Assignment "+str(A+1)+"_pst.csv", "w")
    for values in data:
        csv.writer(a, delimiter=",").writerow(values)
    a.close()
