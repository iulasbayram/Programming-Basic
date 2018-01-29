
import random

def random_list():
    women_file=open("women heroes.txt","r")
    sub_list1=[]
    for line1 in women_file:
        line1=line1.rstrip("\n")
        line1=line1.split(": ")
        line1=", ".join(line1)
        line1=line1.split(", ")
        sub_list1.append(line1)

    women_file.close()


    men_file=open("men heroes.txt","r")
    sub_list2=[]
    for line2 in men_file:
        line2=line2.rstrip("\n")
        line2=line2.split(": ")
        line2=", ".join(line2)
        line2=line2.split(", ")
        sub_list2.append(line2)

    men_file.close()

    return sub_list1, sub_list2

women_list, men_list = random_list()
for i in women_list:
    for j in i:
        if j=="Star-Lord":
            a=i.index(j)
            i.remove(j)
            i.insert(a,"Star Lord")

def updated_list():

    men_list_copy=[]
    for copy1 in men_list:
        men_list_copy.append(copy1)

    women_list_copy=[]
    for copy2 in women_list:
        women_list_copy.append(copy2)

    invited_men_list=[]
    for i in range(5):
        a=random.choice(men_list_copy)
        b=a[0]
        men_list_copy.remove(a)
        invited_men_list.append(b)
    print
    print "Invited men's list is " , invited_men_list

    invited_women_list=[]
    for j in range(5):
        x=random.choice(women_list_copy)
        y=x[0]
        women_list_copy.remove(x)
        invited_women_list.append(y)
    print
    print "Invited women's list is " , invited_women_list

    updated_men_marvel_list=[]
    updated_men_marvel_sublist=[]
    for v in invited_men_list:
        for w in men_list:
            if v==w[0]:
                updated_men_marvel_sublist.append(w)
    updated_men_marvel_list.append(updated_men_marvel_sublist)
    updated_men_marvel_list=updated_men_marvel_list[0]

    men_marvel_list=[]
    men_marvel_sublist=[]
    for xx in updated_men_marvel_list:
        men_marvel_sublist.append(xx[0])
        for xxx in xx[1:]:
            if xxx in invited_women_list:
                men_marvel_sublist.append(xxx)
    men_marvel_list.append(men_marvel_sublist)

    men_marvel_list=men_marvel_list[0]

    updated_men_list=[]
    for yy in range(5):
        updated_men_list.append(men_marvel_list[:6])
        del men_marvel_list[:6]
    print
    print "Updated list for men " , updated_men_list

    updated_women_marvel_list=[]
    updated_women_marvel_sublist=[]
    for r in invited_women_list:
        for t in women_list:
            if r==t[0]:
                updated_women_marvel_sublist.append(t)
    updated_women_marvel_list.append(updated_women_marvel_sublist)
    updated_women_marvel_list=updated_women_marvel_list[0]

    women_marvel_list=[]
    women_marvel_sublist=[]
    for aa in updated_women_marvel_list:
        women_marvel_sublist.append(aa[0])
        for aaa in aa[1:]:
            if aaa in invited_men_list:
                women_marvel_sublist.append(aaa)
    women_marvel_list.append(women_marvel_sublist)
    women_marvel_list=women_marvel_list[0]

    updated_women_list=[]
    for bb in range(5):
        updated_women_list.append(women_marvel_list[:6])
        del women_marvel_list[:6]
    print
    print "Updated list for women ", updated_women_list
    return invited_women_list , invited_men_list , updated_women_list , updated_men_list

invited_women, invited_men , updated_women , updated_men = updated_list()

def random_relationship(invited_w, list_m,count):
    if invited_w== [] :
        print
        x= "Match is finished"
        return x
    else:
        if list_m[count][1] in invited_w:
            print
            print "Day" , str(count+1), "has been selected " , list_m[count][1] , "and" , list_m[count][0]
            print
            print "All happiness is yours"
            b=list_m[count][1]
            invited_w.remove(b)
            return random_relationship(invited_w,list_m,count+1)
        elif list_m[count][2] in invited_w:
            print
            print "Day" , str(count+1), "has been selected " , list_m[count][1] , "and" , list_m[count][0]
            print
            print "All happiness is yours"
            b=list_m[count][1]
            invited_w.remove(b)
            return random_relationship(invited_w,list_m,count+1)

count=0
print random_relationship(invited_women,updated_men,count)
