from random import randint

myListLen = 50

# start with an empty list
myListOfNumbers = []
for index in range(myListLen):
#   print index                                                                 
    myListOfNumbers.append(index)
#    continue          

currLengthOfList = 50

myrandomList = []

for index in range(myListLen):
   # pick a random number in the range (0, currLengthOfList)                    
    my_random_num = randint(0, currLengthOfList - 1)
    currLengthOfList = (currLengthOfList - 1)
    
    # pop that number                                                           
    popped_number = myListOfNumbers.pop(my_random_num)

    myrandomList.append(popped_number)

    

print(myrandomList)

