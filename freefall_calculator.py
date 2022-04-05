import math

# the time of the fall:
t=7.93

# environmental variables: 
g=9.8 # earth
speedOfSound=343 # the speed of sound in dry air at 20 degC

# accuracy:
sigma = 0.004
guessLimit=1000

# set a semi arbitrary max distance guess. if you knew the object's terminal velocity it would be possible to make a more accurate maximum guess
myMax=t*speedOfSound
# set a min distance guess (what if all the time was fall time?) # the actual min will be less than that. it should be that minus the amount of time it would take sound to travel the same distance. haven't thought that through all the way so going with zero
# set a minimum distacne guess of 0
myMin = 0
myGuess= myMax+myMin/2

i=0
error= math.sqrt(2*(myGuess/g))+(myGuess/speedOfSound) - t 
while(abs(error) > sigma and i < guessLimit):
    if error < 0 : # {we need a new min}
        #print("*********************\nguess number: "+str(i)+" negative error. \nold guess: "+str(myGuess)+"\nold min: "+str(myMin)+"\nold max: "+str(myMax))
        myMin=myGuess
        myGuess = (myGuess + myMax)/2
        #print("\nnew guess: "+str(myGuess)+"\nnew min: "+str(myMin)+"\nnew max: "+str(myMax))
    else: # {we need a new max}
        #print("*********************\nguess number: "+str(i)+" positive error. \nold guess: "+str(myGuess)+"\nold min: "+str(myMin)+"\nold max: "+str(myMax))
        myMax = myGuess
        myGuess = (myGuess + myMin)/2
        #print("\nnew guess: "+str(myGuess)+"\nnew min: "+str(myMin)+"\nnew max: "+str(myMax))

    i=i+1 
    error = math.sqrt(2*(myGuess/g))+(myGuess/speedOfSound) - t

print("num of guesses: "+str(i))
print("the distance was approx: "+str(myGuess)) # not sure how to determine the error in meters precisely. What we actually know is that a fall from this height would take within sigma seconds. To figure the error in distance you could calculate how far it would fall in sigma seconds using the end velocity and speed of sound