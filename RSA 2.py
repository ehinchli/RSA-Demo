#Evan Hinchliffe - Spelling errors likley
#Very basic demo of RSA
import math
import time
#------------------------------------------------------
#Reciever 

#primes
p1 = 1000000711
p2 = 1000000801

n = p1*p2  #hard to find factors


phi = (p1-1)*(p2-1)  #need factors to calculate



#must be coprime to phi (share no factors)
e=3
while math.gcd(e,phi) != 1:
    e+=1
 

#find k such that d is an integer
k = 1 
while (k * phi +1)%e != 0: 
    k+=1

#Our private key!!
d = (k * phi +1)//e

#publish n and e as public key
print('\n\nEveryone sees public key: n',n, 'and e',e)






#----------------------------------------------------
#Sender 


message = int(input("Enter an integer (It is the message you are sending): "))

#Uses public key to encode message 
gibberish = (message**e) % n

# send out c
print('Middle man sees gibberish:',gibberish)




#-----------------------------------------------------



#Reciever

#decoding
#pow is c^d mod n .... but faster. 
output = pow(gibberish,d,n) 

print("The message received",output)


###############################



print(input('Hit enter to run factor finder...'))
start= time.time()
i = 3
while i*i<=n: #checks up to around square root of n


    if n%i == 0:
        f1= i
        f2= n//i
        break
    
    i+=2 #skipping even numbers
    
    
print("Factors are",f1," and ",f2)
print("Took", time.time()-start , "Seconds")