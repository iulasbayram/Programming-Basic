# Student Name: Ismail Ulas Bayram
# Student ID: 220201040

# Function 5
# Below that, read_file function is written for reading to file with iterative way.
def read_file():
    file_text=open("Nucleic Acid File.txt","r")
    list1=[]
    for line in file_text:
        sub_list1=[]
        for i in line.split():
            sub_list1.append(i)
        list1.append(sub_list1)
    file_text.close()
    return list1

# Function 1
# Below that, I wrote for checking whether parts of gene with recursive way.
def valid_or_not(dna,nucleic_elements):
    if dna=="":
        return "Valid"
    elif dna[0] not in nucleic_elements:
        return -1
    elif "T" in dna:
        if "U" in dna:
            return -1
        else:
            return valid_or_not(dna[1:],nucleic_elements)
    else:
        return valid_or_not(dna[1:],nucleic_elements)

# Function 2
# Below that, I wrote this function for checking what they are with recursive way.
def DNA_or_RNA(component):
    if component=="":
        return True
    elif component[0]=="U":
        return False
    else:
        return DNA_or_RNA(component[1:])

# Function 3
# Below that, If component is RNA , I wrote this function for converting to DNA with recursive way.
def convert_to_RNA(component):
    if component=="":
        return component
    else:
        if component[0]=="A":
            return "T" + convert_to_RNA(component[1:])
        elif component[0]=="U":
            return "A" + convert_to_RNA(component[1:])
        elif component[0]=="G":
            return "C" + convert_to_RNA(component[1:])
        elif component[0]=="C":
            return "G" + convert_to_RNA(component[1:])

# Function 4
# Below that, I wrote this function to find value of different nucleic acids with recursive way.
# If count of one is more that other one, count of remaining nucleic acid is added with previous count.
def differences(component1,component2,x):
    if component1=="":
        x += len(component2)
        return x
    elif component2=="":
        x += len(component1)
        return x
    elif component1[0]!=component2[0]:
        x=x+1
        return differences(component1[1:],component2[1:],x)
    else:
        return differences(component1[1:],component2[1:],x)

# Function 6
# Below that, I wrote this function to append implemented process in file with iterative way.
def writing(arg):
    file_text=open("Nucleic Acid File.txt","w+")
    for i in arg:
        ll=" ".join(i)
        file_text.write(ll+"\n")
    file_text.close()

# I CONSTITUTE MAIN STRUCTURE FOR USING TO FUNCTIONS ALL TOGETHER.
# I described functions under and I used while and for loops to assign to values.

list_nucleic_acid=read_file()

nucleic_elements=["A","U","T","G","C"]

valid_or_not_list=[]
for i in list_nucleic_acid:
    sub_list=[]
    for a in i:
        x=valid_or_not(a,nucleic_elements)
        sub_list.append(x)
    valid_or_not_list.append(sub_list)

c=0
b=0
dna_list=[]
while c< len(list_nucleic_acid) and b< len(valid_or_not_list):
    if valid_or_not_list[b][0]=="Valid" and valid_or_not_list[b][1]=="Valid":
        dna_list.append(list_nucleic_acid[c])
    b += 1
    c += 1

dna_or_rna_list=[]
for t in dna_list:
    sub_list1=[]
    for r in t:
        sub_list1.append(DNA_or_RNA(r))
    dna_or_rna_list.append(sub_list1)

s=0
d=0
while s < len(dna_list) and d < len(dna_or_rna_list):
    if dna_or_rna_list[d][0]==False:
        aa=dna_list[s][0]
        bb=convert_to_RNA(aa)
        dna_list[s][0]=bb
    elif dna_or_rna_list[d][1]==False:
        cc=dna_list[s][1]
        ee=convert_to_RNA(cc)
        dna_list[s][1]=ee
    s += 1
    d += 1

component_list=[]
for f in dna_list:
    count=0
    component1=f[0]
    component2=f[1]
    component_list.append(differences(component1,component2,count))

h=0
while h < len(dna_list):
    if dna_list[h] in list_nucleic_acid:
        transfer_valid=dna_list[h]
        hh=list_nucleic_acid.index(transfer_valid)
        sub_component_list=component_list[h]
        list_nucleic_acid[hh].append(str(sub_component_list))
    h=h+1

j=0
while j < len(valid_or_not_list):
    if valid_or_not_list[j][0]== -1 or valid_or_not_list[j][1]== -1:
        list_nucleic_acid[j].append("-1")
    j=j+1

writing(list_nucleic_acid)