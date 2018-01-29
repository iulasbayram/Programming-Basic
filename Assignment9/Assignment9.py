# Student Name: Ismail Ulas Bayram
# Student ID: 220201040

# FUNCTION 1
# Function 1 was written to read file
def read_file():
    file_text=open("Students Grades File.txt","r")
    read_list=[]
    for line in file_text:
        print line
        line=line.rstrip("\n")
        print line
        line=line.split(": ")
        print line
        line=" ".join(line)
        print line
        line=line.split("; ")
        print line
        line=" ".join(line)
        print line
        line=line.split(" ")
        read_list.append(line)
    file_text.close()
    return read_list

# Function 2
# Below that, I wrote this function to calculate average value with recursive way.
def calculate_average_grade(grade,n,average_grade):
    if len(grade)==0:
        return average_grade
    else:
        if n <= 2:
            average_grade=average_grade + 0.20 * float(grade[0])
            return calculate_average_grade(grade[1:],(n+1),average_grade)
        elif n==3:
            average_grade= average_grade + 0.40 * float(grade[0])
            return calculate_average_grade(grade[1:],(n+1),average_grade)
        elif 3 < n <= 7:
            average_grade = average_grade + 0.05 * float(grade[0])
            return calculate_average_grade(grade[1:],(n+1),average_grade)

# Function 3
# Below that, I wrote this function to convert letter grade from average grade with recursive way.
def letter_grade(list,letter_list):
    if len(list)==0:
        return letter_list
    else:
        if 100 >= list[0] >= 90:
            letter="AA"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)
        elif 89 >= list[0] >= 85:
            letter="BA"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)
        elif 85 > list[0] >= 80:
            letter="BB"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)
        elif 80 > list[0] >= 75:
            letter="CB"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)
        elif 75 > list[0] >= 70:
            letter="CC"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)
        elif 70 > list[0] >= 65:
            letter="DC"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)
        elif 65 > list[0] >= 60:
            letter="DD"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)
        elif 60 > list[0] >= 50:
            letter="FD"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)
        elif 50 > list[0] >= 0:
            letter="FF"
            letter_list.append(letter)
            return letter_grade(list[1:],letter_list)

# Function 4
# Below that, I wrote this function to sort average grades in list.
def sort_recursively(list,sorted_list):
    if len(list)==0:
        return sorted_list
    else:
        max_value=max(list)
        sorted_list.append(max_value)
        list.remove(max_value)
        return sort_recursively(list,sorted_list)

# Function 5
# Below that, I wrote last function to write in file again with iterative way.
def writing_to_file(list):
    file_text=open("Students Grades File.txt","w")
    for i in list:
        text=" ".join(i)
        file_text.write(text+"\n")
    file_text.close()

# BELOW THAT, I USED ALL FUNCTIONS TO ARRANGE TO ANOTHER VALUES. BASICALLY, I CONSTITUTE "MAIN PROCESS"
read_list=read_file()
print read_list

average_grade=0.0
average_grade_list=[]
for i in read_list:
    n=1
    consequence=calculate_average_grade(i[1:],n,average_grade)
    average_grade_list.append(consequence)

letter_grade_list=[]
letter_grade(average_grade_list,letter_grade_list)

name_list=[]
for sublist in read_list:
    name_list.append(sublist[0])

average_list=[]
for join in range(0,20):
    sub_average_list=[]
    sub_average_list.append(name_list[join])
    sub_average_list.append(average_grade_list[join])
    sub_average_list.append(letter_grade_list[join])
    average_list.append(sub_average_list)

sorted_grade_list=[]
sort_recursively(average_grade_list,sorted_grade_list)

sorted_average_list=[]
for y in sorted_grade_list:
    for x in average_list:
        if y==x[1]:
            sorted_average_list.append(x)

for string in range(len(sorted_average_list)):
    sorted_average_list[string][1]=str(sorted_average_list[string][1])
    sorted_average_list[string][0]+=":"
    sorted_average_list[string][1]+=";"

writing_to_file(sorted_average_list)