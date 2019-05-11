#!/usr/bin/python3
import subprocess as sub
import shlex
import os
import sys
import re

print("Welcome to Secure Linux Application Verifier!")
print("Press 1 for vulnerabilty scanning\nPress 2 for securely compile your source c program\n3.CSP extractor\n4.Flag Finder for Executable File")

choice=int(input("Enter your choice:"))

if(choice==1):
    sub.call(shlex.split('./lynis audit system'))

elif(choice==2):
    path=input("Enter the path of file:")
    if(os.path.exists(path)):
        verify_file=os.path.split(path)[1]
        if(verify_file.endswith(".c")):
            s='gcc '
            print("Enter the level of security you want: ")
            print("1.Basic security\n2.Intermediate Security\n3.Maximum Security")
            sec_level=int(input())

            if(sec_level==1):
                flag="-fstack-protector-all -O -D_FORTIFY_SOURCE=2 -grecord-gcc-switches -g -O2 -frecord-gcc-switches "
                sub.call(shlex.split(s+flag+path))
                #print("The source code has been securely compiled successfully!")

            elif(sec_level==2):
                flag='''-Wformat -Wformat-security -Werror  -fstack-protector-all -O -D_GLIBCXX_ASSERTIONS -fasynchronous-unwind-tables
                 -fexceptions -Werror=implicit-function-declaration -pie -fPIE -grecord-gcc-switches -g -O2 -frecord-gcc-switches '''
                sub.call(shlex.split(s+flag+path))
                #print("The source code has been securely compiled successfully!")

            elif(sec_level==3):
                flag = '''-Wformat -Wformat-security -Werror  -fstack-protector-all -O -D_FORTIFY_SOURCE=2 -D_GLIBCXX_ASSERTIONS -fasynchronous-unwind-tables
                            -fexceptions -Werror=implicit-function-declaration -pie -fPIE -grecord-gcc-switches -g -O2 -frecord-gcc-switches '''
                sub.call(shlex.split(s+flag+path))
                #print("The source code has been securely compiled successfully!")
            else:
                print("Invalid choice, exiting!")
        else:
            print("Bad file or bad path")
    else:
        print("bad path")
elif(choice==3):
    print("Enter the path from where you want to extract the CSPs")
    path_CSP=input()
    if(os.path.exists(path_CSP)):
        print("The following are the email Ids which can be a CSP: ")
        cmd_string=r'''egrep -ho "[[:graph:]]+@[[:graph:]]+" '''
        sub.call([(cmd_string+path_CSP+"*")],shell=True)

elif(choice==4):
    path=input("Enter the path of executable file file:")
    if(os.path.exists(path)):
        cmd = "readelf -p .GCC.command.line " + path
        sub.call(shlex.split(cmd))
    #print("Work in progress")
