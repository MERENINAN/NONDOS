import os
import time

banner = """
███╗   ██╗ ██████╗ ███╗   ██╗    ██████╗  ██████╗ ███████╗
████╗  ██║██╔═══██╗████╗  ██║    ██╔══██╗██╔═══██╗██╔════╝
██╔██╗ ██║██║   ██║██╔██╗ ██║    ██║  ██║██║   ██║███████╗
██║╚██╗██║██║   ██║██║╚██╗██║    ██║  ██║██║   ██║╚════██║
██║ ╚████║╚██████╔╝██║ ╚████║    ██████╔╝╚██████╔╝███████║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝  ╚═════╝ ╚══════╝ for Windows
"""

print(banner)

print("""
noncmd - Command Prompt
noncreater - Create Your File
noncalc - Calculator
""")

whatyouwant = input("What Do You Want ---> ")

if whatyouwant == "noncreater":
    print("""Languages :
Vbs
Perl
Ruby
Python
C
C++
C#
Php
Html""")
    language = input("Language ---> ")
    if language == "Vbs":
        filevbs = open("nondosvbsfile.vbs","w")
        print("File Created (File Name: nondosvbsfile.vbs)")
    if language == "Perl":
        fileperl = open("nondosperlfile.pe","w")
        print("File Created (File Name: nondosperlfile.pe)")
    if language == "Ruby":
        fileruby = open("nondosrubyfile.rb","w")
        print("File Created (File Name: nondosrubyfile.rb)")
        whatyouwant = input("What Do You Want ---> ")
    if language == "Python":
        fileruby = open("nondospythonfile.py","w")
        print("File Created (File Name: nondospythonfile.py)")
        whatyouwant = input("What Do You Want ---> ")
    if language == "C":
        fileruby = open("nondoscfile.c","w")
        print("File Created (File Name: nondoscfile.c)")
        whatyouwant = input("What Do You Want ---> ")
    if language == "C++":
        fileruby = open("nondoscppfile.cpp","w")
        print("File Created (File Name: nondoscppfile.cpp)")
        whatyouwant = input("What Do You Want ---> ")
    if language == "C#":
        fileruby = open("nondoscsfile.cs","w")
        print("File Created (File Name: nondoscsfile.cs)")
        whatyouwant = input("What Do You Want ---> ")
    if language == "Php":
        fileruby = open("nondosphpfile.php","w")
        print("File Created (File Name: nondosphpfile.php)")
        whatyouwant = input("What Do You Want ---> ")
    if language == "Php":
        fileruby = open("nondosphpfile.php","w")
        print("File Created (File Name: nondosphpfile.php)")
        whatyouwant = input("What Do You Want ---> ")
    if language == "Html":
        fileruby = open("nondoshtmlfile.html","w")
        print("File Created (File Name: nondoshtmlfile.html)")
        whatyouwant = input("What Do You Want ---> ")


if whatyouwant == "noncalc":
    print("""Formulas :
+
-
/""")
    formulas = input("Formula ---> ")
    if formulas == "+":
        number1plus = input("Number 1 ---> ")
        number2plus = input("Number 2 ---> ")
        print(number1plus + number2plus)
        time.sleep(9999)
    if formulas == "-":
        number1eksi = input("Number 1 ---> ")
        number2eksi = input("Number 2 ---> ")
        print(number1eksi - number2eksi)
        time.sleep(9999)
    if formulas == "-":
        number1bolu = input("Number 1 ---> ")
        number2bolu = input("Number 2 ---> ")
        print(number1bolu - number2bolu)
        time.sleep(9999)


if whatyouwant == "noncmd":
    print("Welcome To Non Command Prompt (For All Commands Write Help.from.nondos)")
    noncmd = input("Command ---> ")
    if noncmd == "Help.from.nondos":
        print("""
        Commands : 
        ping.website::google.com.from.nondos
        ping.website::youtube.com.from.nondos
        ping.select.website.from.nondos
        """)
        noncmd = input("Command ---> ")
    if noncmd == "ping.website::google.com.from.nondos":
        os.system("ping google.com")
        time.sleep(0.5)
        noncmd = input("Command ---> ")
    if noncmd == "ping.website::youtube.com.from.nondos":
        os.system("ping youtube.com")
        time.sleep(0.5)
        noncmd = input("Command ---> ")
    if noncmd == "ping.select.website.from.nondos":
        pingselect = input("Website ---> ")
        os.system("ping ",pingselect)
        time.sleep(0.5)
        noncmd = input("Command ---> ")
    