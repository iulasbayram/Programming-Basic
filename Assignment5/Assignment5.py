# Student Name: Ismail Ulas Bayram
# Student ID: 220201040

# Below that, I used True-False condition for checking sequence of nucleid acid.
# And then, I wrote extra while loop in "while flag" because extra while loop check whether contituent list is suitable or not.
flag_1= True
while flag_1 :
    print "Please take just 4 constituents.\n C : Cytosine\n G : Guanine\n A : Adenine\n T : Tyhmine\n U : Uracil"
    print
    print "Don't forget: Tyhmine and Uracil are never side by side and every each constituent will be used at least 1"
    constituent1 = (raw_input("Take a constituent").upper())
    count_control=0
    required_nucleid_acid=["A","T","C","G","U"]
    sub_flag1= True
    while count_control < len(constituent1) and sub_flag1 :
        if ("T" in constituent1) and ("U" in constituent1):
            print "You doesn't use Uracil and Tyhmine side by side. Please try again."
            sub_flag1= False

        if constituent1[count_control] in required_nucleid_acid:
            count_control += 1
        else:
            "You enter wrong nucleid acid. Please try again."
            sub_flag1= False
    if sub_flag1== False:
        flag_1= True
    else:
        flag_1= False
constituent1=list(constituent1)

print
print "The constituent 1 is " , constituent1
print

flag_2= True
while flag_2 :
    print "Please take just 4 constituents.\n C : Cytosine\n G : Guanine\n A : Adenine\n T : Tyhmine\n U : Uracil"
    print
    print "Don't forget: Tyhmine and Uracil are never side by side and every each constituent will be used at least 1"
    constituent2 = (raw_input("Take a constituent").upper())
    count_control=0
    required_nucleid_acid=["A","T","C","G","U"]
    sub_flag2= True
    while count_control < len(constituent2) and sub_flag2 :
        if ("T" in constituent2) and ("U" in constituent2):
            print "You doesn't use Uracil and Thymine side by side. Please try again."
            sub_flag1= False

        if constituent2[count_control] in required_nucleid_acid:
            count_control += 1
        else:
            "You enter wrong nucleid acid. Please try again."
            sub_flag2= False
    if sub_flag2== False:
        flag_2= True
    else:
        flag_2= False
constituent2=list(constituent2)

print
print "The constituent 2 is " , constituent2
print

# Below that, I wrote function of checking. The my purpose is checked whether constituent is DNA or not.
def checking(constituent):
    a = 0
    while a < len(constituent):
        if constituent[a] == "T":
            decision= True
            return decision
            break
        else:
            decision=False
        a +=1
    return decision

checking_c1=checking(constituent1)
checking_c2=checking(constituent2)

# Below that, I wrote while loop in function of transformation -
# because according to answer that comes from function of checking, constituent is converted RNA to DNA.
def transformation(checking_c,constituent):
    if checking_c== False:
        decision_count=0
        while decision_count < len(constituent):
            if constituent[decision_count]=="A":
                constituent[decision_count]="T"
            elif constituent[decision_count]=="U":
                constituent[decision_count]="A"
            if constituent[decision_count]=="G":
                constituent[decision_count]="C"
            elif constituent[decision_count]=="C":
                constituent[decision_count]="G"
            decision_count += 1
        print constituent , " -> It was converted RNA to DNA successfully"
    elif checking_c== True:
        print constituent , " -> It was not converted because it doesn't include Uracil."
    return constituent


new_constituent1= transformation(checking_c1,constituent1)
new_constituent2= transformation(checking_c2,constituent2)

# Below that, I used max-min to determine maximum list or minimum list.
def similarity(x,y):
    max_list=max(x,y)
    min_list=min(x,y)
    max_length_list=len(max(x,y))
    min_length_list=len(min(x,y))
    total_circulation=max_length_list - min_length_list + 1 #I wrote total circulation to use in while loop.
    similarity_list=[]
    i=0
    maximum=0
    while i < total_circulation:
        similarity_list.append(max_list[i:(min_length_list + i)])
        i=i+1
    a=0
    while a < total_circulation:
        similarity_rate_list=[]
        if similarity_list[a]==min_list:     # If sub-list is equal to minimum list. Directly, rate of similarity excellent.
            print "Similarity is excellent!"
            print "Similarity rate is %100.0"
            print
            print "If similarity rate is %100, please don't care about below condition."
            break
        elif similarity_list[a]!=min_list:
            e=0
            while e < len(min_list):
                if similarity_list[a][e]==min_list[e]:
                    similarity_rate_list.append(min_list[e])
                    b=(float(len(similarity_rate_list))/min_length_list)*100 # I defined "maximum" to find maximum similarity rate.
                    if b > maximum :                                      # Maximum rate of similarity list is equal to "maximum" so maximum value is taken by "maximum".
                        maximum=b
                e=e+1
        a=a+1
    print
    print "Similarity rate is " , maximum

similarity(new_constituent1,new_constituent2)
















