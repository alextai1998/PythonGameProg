import csv

studentid = {"Chang, Stephanie": "20140800050", "Chen, Cici": "20120700011", "Chiang, Darren": "20070200002",
             "Ho, Sabrina": "20141000057", "Huang, Daniel": "20140900054", "Tai, Alex": "20120800023"}

# Opens google file for reading and then stores values into a list variable
g = open("GoogleActivities.csv")
gcData = [row for row in csv.reader(g)]
g.close()

# Opens google file for reading and then stores values into a list variable
p = open("PowerSchool Template.csv")
psData = [row for row in csv.reader(p)]
p.close()

for A in range(len(gcData[0])-3):  # Iterates number of assignments
    data = [("Teacher Name: ", psData[0][1]), ("Section: ", psData[1][1]), ("Assignment Name: ", gcData[0][3+A]),
            ("Due Date: ", gcData[1][3+A]), ("Points Possible: ", "10", ""), ("Extra Points: ", "0", ""),
            ("Score Type: ", "Points", ""), ("Student ID", "Student Name", "Points")]

    for S in range(len(gcData)-3):  # Iterates number of students
        studentName = gcData[3+S][1] + ", " + gcData[3+S][0]
        points = int(gcData[3+S][3+A])/10
        data.append((studentid[studentName], studentName, points))

    # Creates powerschool file from google file data
    a = open("Assignment "+str(A+1)+".csv", "w")
    for values in data:
        csv.writer(a, delimiter=",").writerow(values)
    a.close()
