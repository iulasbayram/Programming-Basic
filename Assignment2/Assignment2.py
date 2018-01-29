__author__ = 'ulasbayram'

def cpu_select():

    print "There are three brand in this store. Intel: 320$ AMD: 300$ IBM: 290$"
    cpu=raw_input("Please, enter the cpu that you want. Intel or AMD or IBM\n")
    if cpu=="Intel" or cpu=="Intel" or cpu=="intel":
        print("You selected Intel. The amount that you pay is 320$\n")

    elif cpu=="AMD" or cpu =="Amd" or cpu=="amd" :
        print("You selected AMD. The amount that you pay is 300$\n")

    elif cpu=="IBM" or cpu=="Ibm" or cpu=="ibm" :
        print("You selected IBM. The amount that you pay is 290$\n")

    else:
        print("You entered undefined brand. Please, try again.\n")

        cpu_select()
    return cpu
# As is seen to upside, I identified brands and I wrote propare comment in "if" loobs.
# Now, I will continue to determine prices of brands
def cpu_price_select(cpu):

    if cpu=="Intel" or cpu=="Intel" or cpu=="intel" :
        cpu_price=320
        return cpu_price
    elif cpu=="AMD" or cpu=="Amd" or cpu=="amd" :
        cpu_price=300
        return cpu_price
    elif cpu=="IBM" or cpu=="Ibm" or cpu== "ibm":
        cpu_price=290
        return cpu_price
    else:
        cpu_price=0
        return cpu_price
# As is seen to upside, i used parameters because it doesn't take a long time. it is sorter.
def gpu_select():
    print "There are three brand in this store. Nvidia: 150$ ATI(AMD): 145$ Intel: 100$"
    gpu=raw_input("Please,enter the gpu that you want. Nvidia or ATI or Intel\n")

    if gpu=="Nvidia"or gpu=="Nvidia" or gpu== "nvidia":
        print( "You selected Nvidia. The amount that you pay is 150$\n")
        gpu_price=150
        return gpu_price

    elif gpu=="Intel" or gpu=="Intel" or gpu=="intel":
        print("You selected Intel. The amount that you pay is 100$\n")
        gpu_price=100
        return gpu_price

    elif gpu=="ATI" or gpu=="Ati" or gpu=="ati":
        print("You selected ATI. The amount that you pay is 145$\n")
        gpu_price=145
        return gpu_price

    else:
        print("You entered undifined brand.Please,try again.\n")

        gpu_select()
    return gpu

# As is seem to upside, I used "return" because I will call this definition again after next step.
def gpu_price_select(gpu):

    if gpu=="NVIDIA" or gpu=="Nvidia" or gpu=="nvidia":
        gpu_price=150
        return gpu_price

    elif gpu=="INTEL" or gpu=="Intel" or gpu=="intel":
        gpu_price=100
        return gpu_price

    elif gpu=="ATI" or gpu=="Ati" or gpu=="ati":
        gpu_price=145
        return gpu_price

    else:
        gpu_price=0
        return gpu_price
# For gpu, i did the same thing that i did previous one.
def storage_device_select():
    print("There are two type of storage device in this store. HDD: 200$ SSD: 300$")
    storage_device=raw_input("Please, enter the type of storage device that you want. HDD or SSD\n")

    if storage_device=="HDD" or storage_device=="Hdd" or storage_device=="hdd" :
        print "You selected HDD. The amount that you pay is 200$.\n"
        storage_device_price=200
        return storage_device_price

    elif storage_device=="SSD" or storage_device=="ssd":
        print "You selected SSD. The amount that you pay is 300$.\n"
        storage_device_price=300
        return storage_device_price

    else:
        print("You entered undefined brand.Please,try again.\n")
        storage_device_price = storage_device_select()
        return storage_device_price
#For storage device, i implemented the same operation.

def ram_amount_select():

    try:
        ram_amount=int(raw_input("Please,enter amount of ram"))
        print (ram_amount)*25 , "your ram cost.\n"
        ram_price=(ram_amount)*25
        return ram_price

    except:

        print("\n")
        ram_price=0
        return ram_price
        ram_amount_select()
# I used try-except because user can enter undefined value or string.

def discount_of_ati(gpu_price):
    discount_value_of_ati=0.1
    discount_cost_of_ati=gpu_price-(gpu_price*discount_value_of_ati)

    print "You selected ATI gpu " +str(gpu_price)+ \
          "so, we made a discount and the new price is " +str(discount_cost_of_ati)
    return discount_cost_of_ati
# I wrote new definition to calculate discount. I did the same operation for intel.
def discount_of_intel(gpu_price):
    discount_value_of_intel=0.05
    discount_cost_of_intel=gpu_price-(gpu_price*discount_value_of_intel)

    print "You selected Intel gpu " +str(gpu_price)+ \
          "so, we made a discount and the new price is " +str(discount_cost_of_intel)
    return discount_cost_of_intel

def bulk_purchase(total_of_price,amount_of_purchase):
    sum=0
    for amount in range(amount_of_purchase):
        if amount<=amount_of_purchase:
            sum=total_of_price+sum
        else:
            break
    print "Your total price that you need pay is "+str(sum)+"\n"
# For bulk purchase in the last of program, i wrote. sum is ineffective value. Sum exist for calculation total price.
def total_price(ram_price,gpu_price,cpu_price,storage_device_price):
    total_price=ram_price+gpu_price+cpu_price+storage_device_price
    print "Total price that you need pay is " +str(total_price)

    if total_price>=800:
        print "You gain free antivirus software because your total price is more than 800 dollars."

    else:
        print
    return total_price
# First of all, i wrote to calculate total price definition in order that the user can not select reduced devices.

def discount_total_price_of_intel(ram_price,discount_cost_of_intel,cpu_price,storage_device_price):

    total_price=ram_price+cpu_price+discount_cost_of_intel+storage_device_price
    print "New total price is " + str(total_price)
    if total_price >800:
        print "You gain free antivirus software because your total price is more than 800 dollar"
    else:
        print

    return total_price
# Second, i wrote discount total price of intel definition in case the user can select reduced devices.
def discount_total_price_of_ati(ram_price,discount_cost_of_ati,cpu_price,storage_device_price):

    total_price=ram_price+cpu_price+discount_cost_of_ati+storage_device_price
    print "New total price is" + str(total_price)
    if total_price >800:
        print("You gain free antivirus software because your total price is more than 800 dollars")

    else:
        print

    return total_price
# And then, i implemented the same operation for ati.

for i in range(2**20):

    try:
        print"You gain discount %10 if you selected cpu of AMD and gpu of ATI.\n"
        print"You gain discount %5 if you selected cpu of INTEL and gpu of INTEL.\n"
        print("if your total price is more than 800 dollars, you gain free antivirus software.\n")

        cpu=cpu_select()
        gpu=gpu_select()
        gpu_price=gpu_price_select(gpu)
        cpu_price=cpu_price_select(cpu)
        storage_device_price=storage_device_select()
        ram_price=ram_amount_select()

        if (cpu=="AMD" and gpu=="ATI") or (cpu=="Amd" and gpu=="Ati") or(cpu=="amd" and gpu=="ati") or (cpu=="AMD" and gpu=="Ati")\
                or (cpu=="AMD" and gpu=="ati") or (cpu=="Amd" and gpu=="ATI") or (cpu=="Amd" and gpu=="ati") or (cpu=="amd" and gpu=="ATI")\
                or (cpu=="amd" and gpu=="Ati"):
            print("You gain discount")

            discount_cost_of_ati=discount_of_ati(gpu_price)
            discount_total_price_of_ati(cpu_price,discount_cost_of_ati,storage_device_price,ram_price)

        elif (cpu=="Intel" and gpu=="Intel") or (cpu=="INTEL" and gpu=="INTEL") or (cpu=="intel" and gpu=="intel") \
                or (cpu=="INTEL" and gpu=="Intel") or (cpu=="INTEL" and gpu=="intel") or (cpu=="Intel" and gpu=="INTEL")\
                or (cpu=="Intel" and gpu=="intel") or (cpu=="intel" and gpu=="INTEL") or (cpu=="intel" and gpu=="Intel") :
            print("You gain discount")

            discount_cost_of_intel=discount_of_intel(gpu_price)
            discount_total_price_of_intel(cpu_price,discount_cost_of_intel,storage_device_price,ram_price)

        else:
            total_price(cpu_price,gpu_price,storage_device_price,ram_price)

        amount_purchase=input("How many product do you want?\n")

        if (cpu=="AMD" and gpu=="ATI") or (cpu=="Amd" and gpu=="Ati") or(cpu=="amd" and gpu=="ati") or (cpu=="AMD" and gpu=="Ati")\
                or (cpu=="AMD" and gpu=="ati") or (cpu=="Amd" and gpu=="ATI") or (cpu=="Amd" and gpu=="ati") or (cpu=="amd" and gpu=="ATI")\
                or (cpu=="amd" and gpu=="Ati"):
            print("Total amount which you need pay :\n")

            discount_cost_of_ati=discount_of_ati(gpu_price)
            total_price_of_ati=discount_total_price_of_ati(ram_price,discount_cost_of_ati,cpu_price,storage_device_price)
            bulk_purchase(total_price_of_ati,amount_purchase)

        elif (cpu=="Intel" and gpu=="Intel") or (cpu=="INTEL" and gpu=="INTEL") or (cpu=="intel" and gpu=="intel") \
                or (cpu=="INTEL" and gpu=="Intel") or (cpu=="INTEL" and gpu=="intel") or (cpu=="Intel" and gpu=="INTEL")\
                or (cpu=="Intel" and gpu=="intel") or (cpu=="intel" and gpu=="INTEL") or (cpu=="intel" and gpu=="Intel"):
            print("Total amount which you need pay :\n")

            discount_cost_of_intel=discount_of_intel(gpu_price)
            total_price_of_intel=discount_total_price_of_intel(ram_price,discount_cost_of_intel,cpu_price,storage_device_price)
            bulk_purchase(total_price_of_intel,amount_purchase)

        else:
            print("Total amount you need pay:\n")

            total_price_normal=total_price(ram_price,gpu_price,cpu_price,storage_device_price)
            bulk_purchase(amount_purchase,total_price_normal)
    except:
        print("You entered undefined brand. Please, try again.\n")
# And, in case this program execute again and again, i used "for".
# I put try-except in "for" loop because the user can enter undefined value.
# I collected all definitions in "for" loob.
    finish_or_continue=raw_input("Are you continue to shopping or not.\n")

    if finish_or_continue=="no" or finish_or_continue=="No" or finish_or_continue=="NO" :
        break

    else:
        print("Please, continue to the shopping :).")
# to continue the program or not, i wrote additional statement.

# Student Name: Ulas Bayram
# Student ID: 220201040