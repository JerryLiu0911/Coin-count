volunteers=[]                                               #list of volunteers
volunteerdata=[]                                            #collected data from the volunteers
newname="yes"
totalbags=0
totalgain=0                                                 #total collected
namedex=0                                                   #index for names/records number of volunteers.
while(newname=="yes"):                                      #while loop to insert new names
        print('\n')
        if len(volunteers)>0:
            print("Current volunteers:",volunteers)         #updates the current list of volunteers
        name=input("enter your name")                       #asking the user to input their name
        if len(volunteers)> 0:
            for i in range(namedex+1):
                    if name==volunteerdata[i][0] :                            #checking if the person has already entered data
                        print("welcome back,",volunteerdata[i][0],"!")
                        gain=float(volunteerdata[i][3])*100                   #fetching data for the person
                        bags=int(volunteerdata[i][1])
                        accuracymean=float(volunteerdata[i][2])/100
                        correct=bags*accuracymean
                        recount="yes"
                        revisit=1                                             #indicator for re-visits
                        visitdex=i                                            #Storing "i" as an index for who it is that revisited
                        print("Your current data:  Bags checked=",bags,"  Accuracy(percentage)=",accuracymean*100,"%  Money collected= £",gain)
                        break
                                
                    else:
                        volunteers.append(name)                               #if it's someone new, append the name into the list and refresh the data
                        gain=0
                        bags=0                                          
                        correct=0
                        namedex=namedex+1
                        revisit=0
                        break
        else:
                    volunteers.append(name)
                    gain=0
                    bags=0                                          
                    correct=0
                    revisit=0
        coins=("1p","2p","5p","10p","20p","50p","£1","£2")          #valid coins
        coinvalue=(1,2,5,10,20,50,100,200)                          #value of the coin stored as an integer 
        weight=[3.56, 7.12, 3.25, 6.5, 5, 8, 8.75, 12]              #weight the bag should be
        valueperbag=[100, 100, 500, 500, 1000, 1000, 2000, 2000]    #total the bag should be
        if bags==0:
            recount="yes"
        while (recount=="yes"):                                     #while loop for recounting multiple bags
                while (1):                                          #while loop for confirming the type of coin in case of error
                    coin=input("Enter the type of coin")
                    index=0
                    for types in coins :                             #validating the coin
                        if coin == types:
                            brake=1
                            break
                        else :
                            brake=0
                    if brake==0 :
                        print("Unidentified coin. Please enter one of the below, ",coins)  #asks the user to enter it again and shows all valid coins
                    else :
                        break
                if coin=="2p":                                                              # Assigning a coin type to an index for the arrays
                    index+=1
                elif coin=="5p":
                    index+=2
                elif coin=="10p":
                    index+=3
                elif coin=="20p":
                    index+=4
                elif coin=="50p":
                    index+=5
                elif coin=="£1":
                    index+=6
                elif coin=="£2":
                    index+=7
                bagweight=float(input("enter the weight of the bag"))   #weight of bag
                coinsinbag=valueperbag[index]/coinvalue[index]          #calculating the coins in that bag
                coinweight=weight[index]/coinsinbag                     #calculating the weight of that coin type
                percentage=bagweight/weight[index]
                if bagweight < weight[index]:
                    difference=weight[index]-bagweight
                    coinsoff= int(difference/coinweight)                #counting how many coins off
                    if coinsoff < 1 :
                        coinsoff=1
                    print("The amount is",coinsoff,"off.")
                elif bagweight > weight[index]:
                    difference=bagweight-weight[index]
                    coinsoff= int(difference/coinweight)
                    if coinsoff < 1 :
                        coinsoff=1
                    print("The amount is",coinsoff,"more.")
                    
                else:
                    print("the weight is correct!")
                    correct=correct+1
                    coinsoff=0
                bags=bags+1                                             #counter for how many bags they've counted(how many iterations they've run)
                gain=gain+(valueperbag[index]*percentage)               #how much money they've collected
                accuracymean=correct/bags                               #their accuracy
                if revisit==1:                                                  #if this is a revisit, data will be updated to the original array of that individual
                    bagschecked=[volunteers[i],bags,accuracymean*100,gain/100] 
                else:
                    bagschecked=[volunteers[namedex],bags,accuracymean*100,gain/100] #or added a new array to the list
                recount=input("Would you like to enter another bag?")                #confirming to calculate another bag
        else:
                if revisit==1:                                           #removing the old array of the same person if revisited
                    volunteerdata.remove(volunteerdata[visitdex])
                volunteerdata.append(bagschecked)
                totalbags=totalbags+bags                                 #adding the money collected from this individual to the total
                totalgain=totalgain+gain/100                             #adding the bags collected from this individual to the total
                if len(volunteers)<6:                                    #checking if the maximum amount of volunteers have been reached.
                    newname=input("Would you like to change to add a different volunteer?") #switching volunteers
                else:
                    newname="no"
else:
        print('\n')
        print("Total bags checked = ",totalbags)
        print("Total gain = £",totalgain)
        showdata=input("Would you like to see the data of the volunteers?") #option for showing data
        if showdata=="no" or showdata=="No":
            print("Thank you for using this service.")
        else:
            print("Sorted by accuracy in descending order is:")
            print("\n")
            a=[]                                                            #an array consisting the accuracy percentages of every volunteer
            for i in range (namedex+1):                                     #namedex+1 indicated how many volunteers there are
                value=float(volunteerdata[i][2])                            
                a.append(value)
            for i in range (namedex+1):
                for j in range (namedex-i):
                    if a[j]<a[j+1]:                                         #bubble sorting the percentages in descending order
                        temp=a[j]
                        a[j]=a[j+1]
                        a[j+1]=temp
            for i in range(namedex+1):
                for j in range(namedex+1-i):                                #presenting data according to the order in 
                        if a[i]==volunteerdata[j][2]:
                            print("Name=",volunteerdata[j][0],"  Bags checked=",volunteerdata[j][1],"  Accuracy(percentage)=",volunteerdata[j][2],"%  Money collected= £",volunteerdata[j][3])
                            print("\n")
                            volunteerdata.remove(volunteerdata[j])
                            break
            print("Thank you for using this service.")

