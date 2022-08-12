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
""")

whatyouwant = input("What Do You Want ---> ")

if whatyouwant == "noncreater":
    print("""Languages :
Perl
Ruby
Python
C
C++
C#
Php
Html""")
    language = input("Language ---> ")
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


if whatyouwant == "noncmd":
    print("Welcome To Non Command Prompt (For All Commands Write Help.from.nondos)")
    noncmd = input("Command ---> ")
    if noncmd == "Help.from.nondos":
        print("""
        Commands : 
        ping.website::google.com.from.nondos
        ping.website::youtube.com.from.nondos
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