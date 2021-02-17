#!/bin/bash
from subprocess import Popen,PIPE,call,check_output
import hashlib
import random
import math
from random import randrange

# This is one of the main function where the salt is created using the name of the WIFI + details as stored by Computer + The Password of the Wifi
def wifisalt():
	#This function just swaps
	def swap(a,b,salt):
	    temp1=salt[a]
	    temp2=salt[b]
	    salt[b]=temp1
	    salt[a]=temp2
	    return
	
	#process2 takes the current Wifi as a process
	process2=Popen(['iwgetid'],stdin=PIPE,stdout =PIPE)
	stdout,stderr=process2.communicate()       #This line basically gives the output of the process  
	#print(stdout)
	stdout=str(stdout)           # It puts the output in a string for python to interpret properly
	stdout=stdout.split('"')     # Here it Splits all the different lines and makes it into an array
	#print(stdout)
	ssid=stdout[1]               # Run the previous line and will see that the name of the output at 1st position is the Wifi Name.
	# print(ssid)
	# This means ssid is the Name of the Wifi
	COMMAND_LINUX = "sudo ls /etc/NetworkManager/system-connections/ | grep "+stdout[1]+" "   # This COMMAND_LINUX checks whether the Wifi is saved within the System so to ensure that this is a verified System and it can proceed.
	output = check_output(COMMAND_LINUX,shell=True)        # Here it takes all the outputs that are there in the Wifi file.
	ouutput=str(output)                                    # It puts the output in a string for python to interpret properly
	#print(output)
	wname = ouutput[2:-3]                                  # This shows the wifi name after trimming the other details.     
	#print(wname)
	
	# If you see in one sight then you may see that ssid and wname is same in case of an UBUNTU OS But  in case of an KALI this set of code that are written must be there as KALI stores them as an extension of .nvconnection from where you have to extract the output.

	COMMAND_LINUX = "sudo cat /etc/NetworkManager/system-connections/"+wname   # This COMMAND_LINUX checks whether the Wifi is saved within the System so to ensure that this is a verified System and it can proceed.
	output = check_output(COMMAND_LINUX,shell=True)        # Here it takes all the outputs that are there in the Wifi file.
	output=output.splitlines()		
	#print(output)	       
	uuid=str(output[2]).split('=')
	#print(uuid)	       
	uuidfinal=str(uuid[1]).strip(" - ")
	#print(uuidfinal)	       
	uuidfinal=uuidfinal.strip(" ' ")                       # Here it takes the uuid that is being stored by the computer as an details of the wifi. 
	if 'psk' in str(output[16]):                            # Here it takes the password that is being stored by the computer as an details of the wifi. 
	    password=str(output[16]).split('=')
	    passwordfinal=str(password[1]).strip(" ' ")
	else:
	    passwordfinal=uuidfinal
	
	#print(passwordfinal)

	salt=ssid+" "+uuidfinal+" "+passwordfinal               #Finally the salt is made

	# Now to increase more encryption the we swap all the characters of swap here and there.
	length=len(salt)
	length=int(length/4)
	salt=list(salt)
	for x in range (length):
	    swap(4*x+1,4*x+2,salt)
	    swap(4*x,4*x+3,salt)
	    swap(4*x,4*x+1,salt)


	salt=''.join(salt)
	salt=salt.encode('utf-8')
	salt=salt.hex()                #Now encoding with utf - 8 and then taking its hex value

	#print(salt)

	rand=str(random.randint(0,1000000))

	pepper=hashlib.md5(rand.encode())      #Using Standard MD5 to encrypt.
	pepper=pepper.hexdigest()
	#print(len(str(pepper)))
	salt=salt+str(pepper)

	num=0
	for i in salt:
	    num=num+ord(i)
	   
	return num 

def decimalToBinary(n):
    rep = ''  	
    while n > 0:  
        rep += str(n%2)
        n = n//2
    return int(rep[::-1])

def binaryToDecimal(binary):
    binary = int(binary, 2)
    return int(binary)

# def rxor(a,b):
#     x = max(a,b)
#     y = min(a,b)
#     diff = len(str(x))-len(str(y))
#     temp = int(y)*pow(10,diff)
#     if diff != 0:
# 	    temp += y//pow(10,(len(str(y))-diff))
#     y = temp
#     result = ''
#     for i in range(len(str(x))):
#         result += str(int(str(x)[i])^int(str(y)[i]))
#     return result

def nthprime(p):
    no= int(p)
    infile = open('primes.txt', 'r')
    lines = infile.readlines()
    count = 0
    for line in lines:
        count+=1
        if count is no:
            return number
    infile.close()
    return 0

#---------------------------------Start Reading from Here----------------------------------
a1 = (input('Enter Message: '))        
   
a=0
#In This loop below; the unicode(ASCII) of each character of a1 is taken out(ord) and then added to 'a' and in order to make it more encrypted we multiply 1000
for i in a1:
    a=a+ord(i)
    a=a*1000
#print(a)
# a is message

# le converts it to binary and then stores the length of the binary string
le=len(str(decimalToBinary(a)))
b = wifisalt()
#b is wifi salt . Remember the word Salt and use it . It is important.

print("---------Encrytion---------")

ul=int('0b111111111',2) #upper limit of random value
ll=int('0b1111',2) #lower limit of random value
d=random.randrange(ll,ul) #random value 
y=a^b 
po=1
for i in range(int(d)):
    po=i*d
    po=po%100000
    y=y^po
#xored with every prime
dy=str(decimalToBinary(d))
while len(dy) is not 9:
    dy = '0'+dy
dy = int('1' + dy)
#10 digit binary of random
dy = int(str(dy) + str(decimalToBinary(y)))
#appended random
dx=str(decimalToBinary(le))
while len(dx) is not 26:
    dx = '0'+dx
    # print("inside-loop")
dx = int('1' + dx)
#converted binary length to 27 digits and these are done in order to get all of same length as by that only the decoding code is applied.
dx='0b'+str(dx)
dx=int(dx,2)
dx=str(decimalToBinary(dx))
dx = int(dx+ str(dy))
dx='0b'+str(dx)
#print(dx)
dx=int(dx,2)
dx=dx*1000
dx=dx+d
print("Your encrypted message: ", dx) #decimal of the encrypted binary





