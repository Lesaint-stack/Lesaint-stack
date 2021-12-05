import sys
import crypt
import time
import os

#!/bin/sh

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
########################################################################
def scriptorun1():
    os.system('clear')
    print(color.FAIL + """ 
                                            @@            @@
    @@@       @@@@@@@  @@@@@@@@     @@@@@@@@  @@ @@@@@@@  @@  @@        @@@@@@@@@@  
    @@@       @@@@@@@@  @@@@@@@@  @@@@@@@@@@@   @@@    @@    @@@@@      @@@@@@@@@@@  
    !@@       !@@       @@!       @@!@    !!@@@    @@!       @@! @@       !@@@!  
    !@!       !@!       !@!                 @!@    !@!       !@!   @!      @!@    
    !!@       !@!@!@!    !@!          !@!@@!@!@    @!!       @!@   !@      !@!     
    !!       !!!!!!!     @!@!     @!!@  @!!!@!    !!!       !@!   !!      !@!    !@!  !!!  !@!  !!!  
    :!!       :!!           :!!   !!:!!    !:!:      !!:     !!:   !!!     :!!   !!:  !!!  !!:  !!!  
    !:!:::::  :!:       :!:  !:!  :!:!    !:!:!    :!:!      :!:   !:!     !:!  :!:  !:!  :!:  !:!  
    :::: ::    ::: :::  ::   :::  :::::: ::::::  :::  :::    :::   ::      :::  ::::: ::   ::   ::  
    :: : ::::  :: :: :   :::::::  :::::::::::::  ::::::::    :::    :      : :   : :  :   ::    :    
    Version -Dev 1.0
    """ + color.END)

text_crypt=crypt.crypt("egg","HX")
def testPass(cryptPass):
    salt=cryptPass[0:2]
    count=0
    dictFile=open("dictionary","r")
    for word in dictFile.readlines():
        word=word.strip('\n')
        cryptWord=crypt.crypt(word,salt)
        count+=1
        if(cryptWord==cryptPass):
            print(color.OKBLUE + "[+]" + color.END, end=' ')
            print("password match found! Password : "+word+"\n")
            break
        print(color.OKBLUE + "[-]" + color.END, end=' ')
        print("{}/107 No matched! password not found!".format(count))
        time.sleep(0.2)
        print("\033[A                               \033[A")
def main():
    scriptorun1()
    time.sleep(1)
    print('Loading Module cracking password ... ',end=' ')
    time.sleep(2)
    print(color.RED + 'Done'+color.END)
    print(color.OKBLUE + '[+] ' +color.END, end=' ')
    print("Loading Module succesfully done ")
    passFile=open("password")
    for line in passFile.readlines():
        if ":" in line:
            user=line.split(':')[0]
            cryptPass=line.split(':')[1].strip(' ')
            cryptPass=crypt.crypt(cryptPass,cryptPass[0:2])
            print(color.OKBLUE + "[*]" + color.END, end=' ')
            print("Cracking password for:  "+user)
            print(cryptPass)
            time.sleep(2)
            testPass(cryptPass)
main()
