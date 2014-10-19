name=input("Hi What is your name \n")
print("Hello ",name,"! Let's play a game\nThink of random number from 1 to 100, and I'll try to guess it!")
big=100
small=1

DecisionVar="No"
count=0
while(DecisionVar.lower()=="No".lower()):
    count=count+1
    number=int((big+small)/2)
    print("Is it", number ,"?")
    DecisionVar=input()
    if(DecisionVar.lower()=="no"):
     print("Is it lessthan ",number, "?")
     YesNo=input()
     if(YesNo.lower()=="yes"):
         big=number-1
     elif(YesNo.lower()=="no"):
         print("Is it greaterthan ",number, "?")
         YesNo=input()
         small=number+1
print ("I found the number in ",count," attempts")


#output:
#Hi What is your name 
#mouni
#Hello  mouni ! Let's play a game
#Think of random number from 1 to 100, and I'll try to guess it!
#Is it 50 ?
#no
#Is it lessthan  50 ?
#Yes
#Is it 25 ?
#no
#Is it lessthan  25 ?
#yes
#Is it 13 ?
#no
#Is it lessthan  13 ?
#no
#Is it greaterthan  13 ?
#yes
#Is it 19 ?
#no
#Is it lessthan  19 ?
#no
#Is it greaterthan  19 ?
#yes
#Is it 22 ?
#no
#Is it lessthan  22 ?
#no
#Is it greaterthan  22 ?
#yes
#Is it 23 ?
#yes
#I found the number in  6  attempts
