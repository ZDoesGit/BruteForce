import string, time, sys, os
from itertools import product
from numpy import loadtxt
from tqdm import tqdm
Guesstimate = input("Enter your password: ") #Little input for the password, went through variations on this
wordlist = loadtxt('PassWList.txt', dtype=str)#Loads the Password file
Number_Of = len(loadtxt('PassWList.txt', dtype=str))#starts counting the passwords in the file
print("Current Passwords to test:", Number_Of)#This prints it

for i in tqdm(range(1), desc = 'Progress Bar'): #Little progress bar, desc adds a string, so I can name it
    def loop(p_word, creation): #Start of the creation of the loop
        for pw in creation:
            if ''.join(pw) == p_word: #Takes all items in an iterable and joins them into one string
                print('\nYour Password:', ''.join(pw)) #prints the password
                return ''.join(pw)
        return False
    try:
        def brutey(password, max_nchar=20): #string + Int
            #if wordlist and not os.path.isfile(wordlist):
                #print('Error: No Such File: "Password Megalist"' )
                #exit(1) #Yeah ignore this, didn't fix this
            print('Going through Password Megalist')
            PlainPass = loadtxt('PassWList.txt', dtype=str)#Loads the password list and starts sorting through it
            PP = [z for z in PlainPass if z == password] #
            if len(PP) == 1:
                return PP #Loop looking to return the password if found

            else:
                print('Password not found in Megalist, generating number passwords')
                for l in range(1, 900):
                    numerator = product(string.digits, repeat=int(l))#Uses product from Itertools to go though ordered pairs of number 1-900
                    print(":%d" % l)#uses %d as place holder for numbers
                    time.sleep(.44)#lil sleepysleep to just slow it down to showcase the print
                    pw = loop(password, numerator)
                    if pw is not False:
                        return pw #If it finds the password it'll return it

    except:
        print("Password Cracking has failed")
        sys.exit(1)
    start = time.time() #just a little recording of how long the cracking took from start to finish after input
    brutey(''+ Guesstimate) #Another method would of been to just put a password in a () for this
    end = time.time()
    distance = end - start
    print("Your password is " + Guesstimate)
    print(" %f seconds!" % (distance))

